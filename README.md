
# List Contributors

A Github Action that will write out the contributors in a repository to a specified markdown file

---

## Action Status

![Contributing to the Contributors](https://github.com/Maanuj-Vora/List-Contributors/workflows/Contributing%20to%20the%20Contributors/badge.svg)

---

### Contributors
<html><table><tr><td align="center"><a href="https://github.com/apps/github-actions"><img src="https://avatars.githubusercontent.com/in/15368?v=4" width="50" alt="apps/github-actions"><br><sub style="font-size:14px"><b>apps/github-actions</b></sub></a></td><td align="center"><a href="https://github.com/Maanuj-Vora"><img src="https://avatars.githubusercontent.com/u/31610859?v=4" width="50" alt="Maanuj Vora"><br><sub style="font-size:14px"><b>Maanuj Vora</b></sub></a></td><td align="center"><a href="https://github.com/MrStanDu33"><img src="https://avatars.githubusercontent.com/u/22714562?v=4" width="50" alt="DANIELS-ROTH Stan"><br><sub style="font-size:14px"><b>DANIELS-ROTH Stan</b></sub></a></td><td align="center"><a href="https://github.com/zepatrik"><img src="https://avatars.githubusercontent.com/u/5354445?v=4" width="50" alt="Patrik"><br><sub style="font-size:14px"><b>Patrik</b></sub></a></td></tr></table></html>

---

## Setting Up The Workflow Run

| Input Tag | Required | Default Value | Example |
|--|--|--|--|
| REPO_NAME | True | N/A | '${{github.repository}}' or Maanuj-Vora/List-Contributors |
| ACCESS_TOKEN | True | N/A | ${{secrets.GITHUB_TOKEN}} |
| CONTRIBUTOR | True | N/A | "### Contributors" |
| FILEPATH | False | '/README.md' | N/A |
| COLUMN_PER_ROW | False | '6' | N/A |
| IMG_WIDTH | False | '100' | N/A |
| FONT_SIZE | False | '14' | N/A | 
| COMMIT_MESSAGE | False | 'Contributed to Contributer' | N/A |

---

### Example

An example of this workflow can be found at `example.yml`
