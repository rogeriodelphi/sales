# import os
# import requests
#
#
# class GithubApi():
#     API_URL = os.environ.get("GITHUB_API_URL", "https://api.github.com")
#     GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
#
#     def _init_(self, org):
#         # self._login = login
#         self._org = org
#
#
#         def get_organization(self):  # login: str
#             """Busca uma organização no Github
#             :login: login da organização no Github
#             """
#             response = requests.get(
#                 f'https://api.github.com/orgs/{self._org}/repos')
#             if response.status_code == 200:
#                 return response.json()
#             else:
#                 return response.status_code
#
#
#         def print_organization(self):
#             dados_api = self.get_organization()
#             if type(dados_api) is not int:
#                 for i in range(len(dados_api)):
#                     print(dados_api[i]['name'])
#             else:
#                 print(dados_api)
#
#
# organizations = GithubApi('github')
# # organizations.print_organization()
#
#
# def get_organization_public_members(self):
#     """Retorna todos os membros públicos de uma organização
#     :login: login da organização no Github
#    """
#     response = requests.get(
#         f'https://api.github.com/orgs/{self._org}/public_members')
#     if response.ok:
#         return len(response.json())
#     else:
#         return response.status_code
#
#
#     def print_members(self):
#         dados_api = self.get_organization_public_members()
#         print(dados_api)
#
#
# # members = GithubApi('git')
# # members.print_members()