from github import Github
import os
import base64


def getInput(input_name):
    return str(os.environ.get('{}'.format(input_name).upper())).strip()


def formatContributors(repo, columnRow, width, font,
                       headFormat, tailFormat):
    USER, HEAD, TAIL, contributors = 0, headFormat, tailFormat, repo.get_contributors()
    for contributor in contributors:
        name, avatarURL, htmlURL = contributor.name, contributor.avatar_url, contributor.html_url
        if name == None:
            name = htmlURL[19:]
        if USER >= columnRow:
            new_tr, HEAD, USER = '', HEAD + new_tr, 0
        HEAD += f'''<td align="center"><a href={htmlURL}><img src={avatarURL} width="{width};" alt={name}/><br /><sub style="font-size:{font}px"><b>{name}</b></sub></a></td>'''
        USER += 1
    return HEAD + TAIL


def writeRepo(repo, contributorList, path, commitMessage, CONTRIB, ENDCONTRIB):
    contents = repo.get_contents('{}'.format(path))
    text_str = (base64.b64decode(contents.content.replace(
        '\n', '')).decode('utf-8')).split(CONTRIB)
    text_str.append((text_str[len(text_str)-1].split(ENDCONTRIB))
                    [len(text_str[len(text_str)-1].split(ENDCONTRIB))-1])
    if len(text_str) <= 2:
        text_str.append("")
    try:
        end = [contributorList, '\n' + text_str[1]]
        text = text_str[0] + CONTRIB + end[0] + \
            '\n\n' + ENDCONTRIB + text_str[len(text_str)-1]
        repo.update_file(contents.path, commitMessage, text, contents.sha)
    except IndexError:
        raise Exception("The file where contributors are trying to be written '" +
                        path + "' does not have '" + CONTRIB + "' section")
    except Exception as e:
        raise Exception(e)


accessToken, repoName, CONTRIBUTOR, ENDCONTRIBUTOR, PATH, COMMIT_MESSAGE = getInput('ACCESS_TOKEN'), getInput(
    'REPO_NAME'), getInput('CONTRIBUTOR') + '\n', getInput('ENDCONTRIBUTOR'), getInput('FILEPATH'), getInput('COMMIT_MESSAGE')

COLUMN_PER_ROW = int(float(getInput('COLUMN_PER_ROW')))

IMG_WIDTH = int(float(getInput('IMG_WIDTH')))

FONT_SIZE = int(float(getInput('FONT_SIZE')))

repo = Github(accessToken).get_repo(repoName)

writeRepo(repo, formatContributors(repo, COLUMN_PER_ROW, IMG_WIDTH,
                                   FONT_SIZE, '<html><table><tr>', '</tr></table></html>'), PATH, COMMIT_MESSAGE,
          CONTRIBUTOR, ENDCONTRIBUTOR)
