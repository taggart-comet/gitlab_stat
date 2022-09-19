import gitlab
import os

class GitlabReviewStat:

    def __init__(self):
        self.gl = gitlab.Gitlab(url=os.environ['GITLAB_URL'], private_token=os.environ['GITLAB_PRIVATE_TOKEN'])

    # набираем аппруверов по всем МР в группе проектов
    def appendForGroup(self, group_id, since, approvers):
        group = self.gl.groups.get(group_id)
        mrs = group.mergerequests.list(state='merged', order_by='created_at', created_after=since, get_all=True)
        print("Analyzing {} MRs from group [{}] since {}..".format(len(mrs), group.attributes['name'], since))

        for group_mr in mrs:
            project = self.gl.projects.get(group_mr.project_id)
            mr = project.mergerequests.get(group_mr.iid)
            mr_approved_by = mr.approvals.get().approved_by
            for mr_approver in mr_approved_by:
                mr_approver_username = mr_approver['user']['username']
                if mr_approver_username in approvers:
                    approvers[mr_approver_username] = approvers[mr_approver_username] + 1
                else:
                    approvers[mr_approver_username] = 1
