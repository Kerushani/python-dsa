# # Part 1
# We frequently send notifications to users related to their subscriptions. Each user has an account creation date and a subscription plan with a specific duration. You'll need to generate email subject lines corresponding to each user for different stages of their subscription, sorted by time.

# Your notification system will need to allow the configuration of a send schedule. For example, a send schedule configuration might be: send one email on the account creation date, another email 15 days before the subscription end date, and a final email on the subscription end date. The send schedule could look something like this:
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
Questions/edge cases:
- format of the output
- should the user_accounts be initalized in the construtor

- end = account_date + duration
- 

Implementation

[
    [day, message],
    [day, message],
    [day, message]
]

loop over user_accounts:
    loop over each key in send_schedule:
        day = ...
        subject_line = " "
        if day > 0:
            output.append([day, subject_line])
"""

class Notifier:
    def __init__(self, user_accounts = None):
        self.user_accounts = user_accounts
    def new(self, send_schedule) -> list:
        message_list = []
        for user_account in self.user_accounts:
            for send_day, subject_line in send_schedule.items():
                start = user_account["account_date"]
                end = user_account["account_date"] + user_account["duration"]
                if send_day == "start":
                    day = start
                elif send_day == "end":
                    day= end
                else:
                    day= user_account["duration"] + int(send_day)
                if day < start:
                    break
                message = f"[{subject_line}] Subscription for {user_account['name']} ({user_account['plan']})"
                message_list.append([day, message])
        message_list.sort(key=lambda message:message[0])
        return message_list


user_accounts = [
    {"account_date": 0, "duration": 30, "name": "John", "plan": "Silver"},
    {"account_date": 1, "duration": 15, "name": "Alice", "plan": "Gold"}
]
notifier = Notifier(user_accounts)
send_schedule = {
    "start": "Welcome",
    "-15": "Upcoming expiry", # 15 days relative to the end, always negative,
    "-16": "Upcoming expiry", # 16 days relative to the end, always negative
    "end": "Expired"
}

# print(notifier.new(send_schedule))

# # Part 2
# Sometimes users may choose to change their plan during their subscription. In this part, you'll have an unsorted list of subscription changes made by users, specifying their name, time of change, and new plan. 
# Each subject line should now indicate the updated plan of the user. For example, if Alice changes her plan from "Gold" to "Platinum" at time 5, her next email should reflect the new plan. We also want to emit an email when a plan is updated.

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
"""
[
    [day, UPDATE, name, new_plan, subject_line],
    [day, UPDATE, name, new_plan, suject_line],
    [day, UPDATE, name, new_plan, subject_line],
]
"""
import collections 
class Notifier:
    def __init__(self, user_accounts = None, subscription_changes = None):
        self.user_accounts = user_accounts
        self.subscription_changes = subscription_changes
    def new(self, send_schedule) -> list:
        message_list = []
        for user_account in self.user_accounts:
            for send_day, subject_line in send_schedule.items():
                start = user_account["account_date"]
                end = user_account["account_date"] + user_account["duration"]
                if send_day == "start":
                    day = start
                elif send_day == "end":
                    day= end
                else:
                    day= end + int(send_day) 
                if day < start:
                    continue
                message_list.append([day, "SCHEDULED", user_account['name'], user_account['plan'], subject_line])
        for subscription_change in subscription_changes:
            new_plan = subscription_change.get("new_plan")
            if new_plan:
                message_list.append([subscription_change["change_date"], "UPDATE", subscription_change['name'], subscription_change['new_plan'], "[Update]"])
        message_list.sort(key=lambda message:(message[0], 0 if message[1] == "UPDATE" else 1))

        # for any names that have an "UPDATE" we want to update their future emails with this new plan
        """
        iterate over each name in the subscription_changes:
            keeep track of the current plan and if the message[1] == "UPDATE", update message[3] for all future emails with the same name
        """
        current_subscription = collections.defaultdict(str)

        for message in message_list:
            if message[1] == "UPDATE":
                current_subscription[message[2]] = message[3]
            else:
                # if the name exists in current_subscription, update the plan with the new plan
                if message[2] in current_subscription:
                    message[3] = current_subscription[message[2]]
        
        # construct a message with [day, message]
        outgoing_messages = []
        for message in message_list:
            outgoing_messages.append([message[0], f"[{message[-1]}] Subscription for {message[2]} {message[3]}"])


        return outgoing_messages


user_accounts = [
    {"account_date": 0, "duration": 30, "name": "John", "plan": "Silver"},
    {"account_date": 1, "duration": 15, "name": "Alice", "plan": "Gold"}
]
notifier = Notifier(user_accounts)
send_schedule = {
    "start": "Welcome",
    "-15": "Upcoming expiry", # 15 days relative to the end, always negative,
    "-16": "Upcoming expiry", # 16 days relative to the end, always negative
    "end": "Expired"
}

subscription_changes = [
	{"change_date": 5, "name": "Alice", "new_plan": "Platinum"},
	{"change_date": 20, "name": "John", "extension_days": 15}
]

print(notifier.new(send_schedule))