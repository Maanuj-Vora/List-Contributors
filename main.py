from github import Github
import os
import base64
import re


def getInput(input_name):
    return os.environ['INPUT_{}'.format(input_name)]


def shapeCode(shape):
    if shape == 'round':
        return 'border-radius: 50%;'
    return ''


def formatContributors(repo, columnRow, width, shape, font,
                       headFormat, tailFormat):
    USER, HEAD, TAIL, contributors = 0, headFormat, tailFormat, repo.get_contributors()
    for contributor in contributors:
        name, avatarURL, htmlURL = contributor.name, contributor.avatar_url, contributor.html_url
        if name == None:
            name = htmlURL[19:]
        if USER >= columnRow:
            USER = 0
        HEAD += f'''<td align="center"><a href={htmlURL}><img src={avatarURL} width="{width};" style="{shapeCode(shape)}" alt={name}/><br /><sub style="font-size:{font}px"><b>{name}</b></sub></a></td>'''
        USER += 1
    return HEAD + TAIL


def writeRepo(repo, contributorList, htmlStart, htmlEnd, path, commitMessage, CONTRIB):
    contents = repo.get_contents('{}'.format(path))
    text_str = (base64.b64decode((contents.content).replace(
        '\n', '')).decode('utf-8')).split(CONTRIB)
    try:
        if re.match(htmlStart, text_str[1]):
            end = text_str[1].split(htmlEnd)
            end[0] = end[0] + htmlEnd
        else:
            end = ['', '\n\n' + text_str[1]]

        if end[0] != contributorList:
            end[0] = contributorList
            text = text_str[0] + CONTRIB + end[0] + end[1]
            repo.update_file(contents.path, commitMessage, text, contents.sha)
        else:
            pass
    except IndexError:
        raise Exception(path + "' does not have '" + CONTRIB)
    except Exception as e:
        raise Exception(e)


accessToken, repoName, CONTRIBUTOR, PATH, COMMIT_MESSAGE = getInput('ACCESS_TOKEN'), getInput(
    'REPO_NAME'), getInput('CONTRIBUTOR') + '\n', getInput('FILEPATH'), getInput('COMMIT_MESSAGE')

COLUMN_PER_ROW = int(getInput('COLUMN_PER_ROW'))
IMG_WIDTH = int(getInput('IMG_WIDTH'))
FONT_SIZE = int(getInput('FONT_SIZE'))
SHAPE = getInput('SHAPE')

github = Github(accessToken)
repo = github.get_repo(repoName)

htmlStart = '<html><table><tr>'
htmlEnd = '</tr></table></html>'

writeRepo(repo=repo, contributorList=formatContributors(repo=repo, columnRow=COLUMN_PER_ROW, width=IMG_WIDTH, shape=SHAPE,
                                                        font=FONT_SIZE, headFormat=htmlStart, tailFormat=htmlEnd), htmlStart=htmlStart, htmlEnd=htmlEnd, path=PATH, commitMessage=COMMIT_MESSAGE,
          CONTRIB=CONTRIBUTOR)
