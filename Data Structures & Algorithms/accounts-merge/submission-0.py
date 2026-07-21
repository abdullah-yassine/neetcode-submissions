class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        def find(a): # finds the root and returns it
            while a != parents[a]:
                a = parents[a]
            return a
        def union(a, b):
            aRoot = find(a)
            bRoot = find(b)
            if aRoot != bRoot:
                parents[aRoot] = bRoot
        parents = {} # email : parents email
        email_to_name = {} # email : name
        for account in accounts:
            emails = account[1:]
            name = account[0]
            anchor = emails[0] # the first email is the anchor or the root
            for email in emails:
                parents.setdefault(email, email)
                parents.setdefault(anchor, anchor)
                email_to_name[email] = name
                union(anchor, email)
        groups = defaultdict(set) # no we need to group the emails of the same account
        for email in email_to_name:
            root = find(email)
            groups[root].add(email)
        result = []
        for root, emails in groups.items():
            name = email_to_name[root]
            result.append([name] + sorted(emails))
        return result

        

