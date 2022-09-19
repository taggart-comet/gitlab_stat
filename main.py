from tabulate import tabulate
from gitlab_review_stat import GitlabReviewStat
from dotenv import load_dotenv

load_dotenv()

approvers = {}
gitlab_stat = GitlabReviewStat()
# gitlab_stat.appendForGroup(48, '2022-09-01', approvers)
# gitlab_stat.appendForGroup(27, '2022-09-01', approvers)
gitlab_stat.appendForGroup(1, '2022-09-01', approvers)

print('Username    | MRs Approved')
approver_items = []
for username in sorted(approvers, key=approvers.get, reverse=True):
    approver_items.append([username, approvers[username]])
print(tabulate(approver_items))
