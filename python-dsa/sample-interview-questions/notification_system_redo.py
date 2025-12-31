# # Part 1
# We frequently send notifications to users related to their subscriptions. Each user has an account creation date and a subscription plan with a specific duration. 
# You'll need to generate email subject lines corresponding to each user for different stages of their subscription, sorted by time.

# Your notification system will need to allow the configuration of a send schedule. 
# For example, a send schedule configuration might be: send one email on the account creation date, another email 15 days before the subscription end date, 
# and a final email on the subscription end date. The send schedule could look something like this:
#           |
# t = start | [Welcome] Subscription for ${user} (${plan})
#           |
#           |
# t=15 days |
# before end| [Upcoming expiry] Subscription for ${user} (${plan})
#           |
#           |
# t = end   | [Expired] Subscription for ${user} (${plan})
#           |
#           ▼

# Given a send schedule configuration, your input will be an unsorted list of unique user accounts with the account creation date, subscription duration in days, user name, and subscription plan. Your objective is to print out the subject lines of all emails we will send out, sorted by time. Your output should include the time, the type of email, the user, and the plan.

# Here's a sample of how your system should behave:

# send_schedule = {
#     "start": "Welcome",
#     "-15": "Upcoming expiry", # 15 days relative to the end, always negative,
#     "-16": "Upcoming expiry", # 16 days relative to the end, always negative
#     "end": "Expired"
# }

# notifier = Notifier.new(send_schedule)

# user_accounts = [
#     {"account_date": 0, "duration": 30, "name": "John", "plan": "Silver"},
#     {"account_date": 1, "duration": 15, "name": "Alice", "plan": "Gold"}
# ]

# (You are welcome to use any data structure you see fit for this problem)

# Output:
# 0: [Welcome] Subscription for John (Silver)
# 1: [Welcome] Subscription for Alice (Gold)
# 1: [Upcoming expiry] Subscription for Alice (Gold)
# 15: [Upcoming expiry] Subscription for John (Silver)
# 16: [Expired] Subscription for Alice (Gold)
# 30: [Expired] Subscription for John (Silver)

"""
- output -> list -> [(sned_date, message), (sned_date, message), (sned_date, message)]
- edge cases:
    - if the send sechdule is -16 and the duration 15 -> we'll get negative value to send out the 
    email in the output
        - filtering out negative send dates
"""

class Notifier:
    def __init__(self, send_schedule, user_accounts):
        self.send_schedule = send_schedule
        self.user_accounts = user_accounts
    def send_emails(self):
        output = []
        for account in self.user_accounts:
            for time, message in self.send_schedule.items():
                if time == "start":
                    output.append((account["account_date"], f'[{message}] Subscription for {account["name"]} {account["plan"]}'))
                elif time == "end":
                    output.append((account["duration"], f'[{message}] Subscription for {account["name"]} {account["plan"]}'))
                else:
                    if account["duration"] + int(time) < 0:
                        continue
                    else:
                        output.append((account["duration"] + int(time), f'[{message}] Subscription for {account["name"]} {account["plan"]}'))

        output.sort(key=lambda email:email[0])
        return output
                

user_accounts = [
    {"account_date": 0, "duration": 30, "name": "John", "plan": "Silver"},
    {"account_date": 1, "duration": 15, "name": "Alice", "plan": "Gold"}
]

send_schedule = {
    "start": "Welcome",
    "-15": "Upcoming expiry", # 15 days relative to the end, always negative,
    "-16": "Upcoming expiry", # 16 days relative to the end, always negative
    "end": "Expired"
}

notifier = Notifier(send_schedule, user_accounts)

# print(notifier.email_output())

# # Part 2
# Sometimes users may choose to change their plan during their subscription. In this part, you'll have an unsorted list of subscription changes made by users, specifying
#  their name, time of change, and new plan. 
# Each subject line should now indicate the updated plan of the user. For example, if Alice changes her plan from "Gold" to "Platinum" at time 5, her next 
# email should reflect the new plan. We also want to emit an email when a plan is updated.

# user_accounts = [
#     {"account_date": 0, "duration": 30, "name": "John", "plan": "Silver"},
#     {"account_date": 1, "duration": 15, "name": "Alice", "plan": "Gold"}
# ]
# subscription_changes = ['
#     {"change_date": 9, "name": "Alice", "new_plan": "platinum"}
#     {"change_date": 5, "name": "Alice", "new_plan": "platinum"}
# ]
# notifier.send_emails(user_accounts, subscription_changes)

# Output:
# 0: [Welcome] Subscription for John (Silver)
# 1: [Welcome] Subscription for Alice (Gold)
# 1: [Upcoming expiry] Subscription for Alice (Gold)
# 5: [Updated] Subscription for Alice (Platinum)
# 15: [Upcoming expiry] Subscription for John (Silver)
# 16: [Expired] Subscription for Alice (Platinum)
# 30: [Expired] Subscription for John (Silver)

# class Notifier:
#     def __init__(self, send_schedule, user_accounts):
#         self.send_schedule = send_schedule
#         self.user_accounts = user_accounts
#     def send_emails(self, subscription_changes):
#         output = []
#         for account in self.user_accounts:
#             for time, message in self.send_schedule.items():
#                 for change in subscription_changes:
#                     if time == "start":
#                         output.append((account["account_date"], f'[{message}] Subscription for {account["name"]} {account["plan"]}'))
#                     elif time == "end":
#                         send_day = account["duration"]
#                         isSubscirptionUpdated = send_day > change["change_date"] and account["name"] == change["name"]
#                         if isSubscirptionUpdated:
#                             output.append((send_day, f'[{message}] Subscription for {account["name"]} {change["new_plan"]}'))
#                         else:
#                             output.append((account["duration"], f'[{message}] Subscription for {account["name"]} {account["plan"]}'))
#                     else:
#                         send_day = account["duration"] + int(time) 
#                         if send_day < 0:
#                             continue
#                         else:
#                             # print(send_day)
#                             # print(change["change_date"])
#                             # print(send_day > change["change_date"])
#                             # print("----")
#                             isSubscirptionUpdated = send_day > change["change_date"] and account["name"] == change["name"]
#                             if isSubscirptionUpdated:
#                                 output.append((send_day, f'[{message}] Subscription for {account["name"]} {change["new_plan"]}'))
#                             else:
#                                 output.append((send_day, f'[{message}] Subscription for {account["name"]} {account["plan"]}'))

#         output.sort(key=lambda email:email[0])
#         return output

class Notifier:
    def __init__(self, send_schedule, user_accounts):
        self.send_schedule = send_schedule
        self.user_accounts = user_accounts
    def send_emails(self):
        output = []
        for account in self.user_accounts:
            for time, message in self.send_schedule.items():
                if time == "start":
                    output.append((account["account_date"], "SCHEDULE", account["name"], f'[{message}] Subscription for {account["name"]} {account["plan"]}'))
                elif time == "end":
                    output.append((account["duration"], "SCHEDULE", account["name"], f'[{message}] Subscription for {account["name"]} {account["plan"]}'))
                else:
                    if account["duration"] + int(time) < 0:
                        continue
                    else:
                        output.append((account["duration"] + int(time), "SCHEDULE", account["name"], f'[{message}] Subscription for {account["name"]} {account["plan"]}'))

        # for change in subscription_changes:
        #     output.append((change["change_date"], "UPDATE", {account["name"]}, {change["new_plan"]}, account["name"], {change["new_plan"}, f'[{message}] Subscription for {account["name"]} {change["new_plan"]}'))


        # we sort the output first and if they have value "UPDATE" then they get sorted first
        output.sort(key=lambda email:email[0])

        # create a hashmap of current plans
        current_plan = {account["name"]: account["plan"] for account in self.accounts}

        # (timestamp, kind, name, plan, payload)
        for timestamp, kind, name, plan, payload in output:
            if kind == "UPDATE":
            # update the current with new plan if there is a change in the plan
                payload = f'[{message}] Subscription for {account["name"]} {change["new_plan"]}'
                current_plan[name]=plan
            else: #SCHEDULED UPDATE
                current_plan[name]=plan

            results.append((timestamp, ))

        return results
"""
- second iteration ecause subscription_changes append the emails array with those new email values
- we want to ceate the events (timsteamp, kind_scedule, name, plan, payload)
- 
"""
user_accounts = [
    {"account_date": 0, "duration": 30, "name": "John", "plan": "Silver"},
    {"account_date": 1, "duration": 15, "name": "Alice", "plan": "Gold"}
]

send_schedule = {
    "start": "Welcome",
    "-15": "Upcoming expiry", # 15 days relative to the end, always negative,
    "-16": "Upcoming expiry", # 16 days relative to the end, always negative
    "end": "Expired"
}

subscription_changes = [
    {"change_date": 9, "name": "Alice", "new_plan": "platinum"},
    {"change_date": 5, "name": "Alice", "new_plan": "platinum"},
]

notifier = Notifier(send_schedule, user_accounts)

print(notifier.send_emails(subscription_changes))



# Part 3
# Users may also choose to extend their plan during their subscription. Thus, the list of subscription changes can also include a change to extend a subscription by a set number of days. This increases the overall duration of the subscription and requires reminders to be rescheduled/re-sent. For example, if John extends his subscription by 15 days after 20 days, he should receive another upcoming expiry email on day 30.

# subscription_changes = [
# 	{"change_date": 5, "name": "Alice", "new_plan": "Platinum"},
# 	{"change_date": 20, "name": "John", "extension_days": 15}
# ]

# Output
# 0: [Welcome] Subscription for John (Silver)
# 1: [Welcome] Subscription for Alice (Gold)
# 1: [Upcoming expiry] Subscription for Alice (Gold)
# 5: [Updated] Subscription for Alice (Platinum)
# 15: [Upcoming expiry] Subscription for John (Silver)
# 16: [Expired] Subscription for Alice (Platinum)
# 20: [Renewed] Subscription for John (Silver)
# 30: [Upcoming expiry] Subscription for John (Silver)
# 45: [Expired] Subscription for John (Silver)




# problem 1

# send_schedule = {
#     "start": "Welcome",
#     "-15": "Upcoming expiry", # 15 days relative to the end, always negative,
#     "-16": "Upcoming expiry", # 16 days relative to the end, always negative
#     "end": "Expired"
# }

# notifier = Notifier.new(send_schedule)

# user_accounts = [
#     {"account_date": 0, "duration": 30, "name": "John", "plan": "Silver"},
#     {"account_date": 1, "duration": 15, "name": "Alice", "plan": "Gold"}
# ]

# (You are welcome to use any data structure you see fit for this problem)

# Output:
# 0: [Welcome] Subscription for John (Silver)
# 1: [Welcome] Subscription for Alice (Gold)
# 1: [Upcoming expiry] Subscription for Alice (Gold)
# 15: [Upcoming expiry] Subscription for John (Silver)
# 16: [Expired] Subscription for Alice (Gold)
# 30: [Expired] Subscription for John (Silver)