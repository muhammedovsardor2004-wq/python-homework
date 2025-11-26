# TASK 1

# --------------------------------------
# ACCOUNT CLASS
# --------------------------------------
class Account:
    def __init__(self, acc_number, holder_name, balance=0):
        self.acc_number = acc_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True
        else:
            return False
    
    def __str__(self):
        return f"Account Number: {self.acc_number}\nHolder: {self.holder_name}\nBalance: {self.balance}\n"


# --------------------------------------
# BANK CLASS
# --------------------------------------
class Bank:
    def __init__(self):
        self.accounts = []

    # Yangi account qo'shish
    def add_account(self, account):
        self.accounts.append(account)
        print("Account added successfully!\n")

    # Accountni raqam orqali topish
    def find_account(self, acc_number):
        for acc in self.accounts:
            if acc.acc_number == acc_number:
                return acc
        return None

    # Balansni ko'rish
    def check_balance(self, acc_number):
        account = self.find_account(acc_number)
        if account:
            print(f"Balance: {account.balance}\n")
        else:
            print("Account not found!\n")

    # Deposit qilish
    def deposit_money(self, acc_number, amount):
        account = self.find_account(acc_number)
        if account:
            account.deposit(amount)
            print("Deposit successful!\n")
        else:
            print("Account not found!\n")

    # Pul yechish
    def withdraw_money(self, acc_number, amount):
        account = self.find_account(acc_number)
        if account:
            if account.withdraw(amount):
                print("Withdrawal successful!\n")
            else:
                print("Insufficient funds! (Overdraft)\n")
        else:
            print("Account not found!\n")

    # Pul o‘tkazish (transfer)
    def transfer_money(self, from_acc, to_acc, amount):
        sender = self.find_account(from_acc)
        receiver = self.find_account(to_acc)

        if sender and receiver:
            if sender.withdraw(amount):
                receiver.deposit(amount)
                print("Transfer successful!\n")
            else:
                print("Insufficient funds! Transfer failed.\n")
        else:
            print("One or both accounts not found!\n")

    # Barcha accountlarni ko'rsatish
    def display_accounts(self):
        print("\n------ ALL ACCOUNTS ------")
        for acc in self.accounts:
            print(acc)


# --------------------------------------
# MAIN PROGRAM (CLI)
# --------------------------------------
def main():
    bank = Bank()

    while True:
        print("\n=== BANK MENU ===")
        print("1. Add Account")
        print("2. Check Balance")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Transfer Money")
        print("6. Display All Accounts")
        print("7. Exit")

        choice = input("Choose an option: ")

        # 1. Account qo'shish
        if choice == "1":
            acc_number = input("Account Number: ")
            holder_name = input("Account Holder Name: ")
            balance = float(input("Initial Balance: "))
            bank.add_account(Account(acc_number, holder_name, balance))

        # 2. Balansni ko‘rish
        elif choice == "2":
            acc_number = input("Enter Account Number: ")
            bank.check_balance(acc_number)

        # 3. Deposit qilish
        elif choice == "3":
            acc_number = input("Enter Account Number: ")
            amount = float(input("Amount to deposit: "))
            bank.deposit_money(acc_number, amount)

        # 4. Pul yechish
        elif choice == "4":
            acc_number = input("Enter Account Number: ")
            amount = float(input("Amount to withdraw: "))
            bank.withdraw_money(acc_number, amount)

        # 5. Pul o‘tkazish (transfer)
        elif choice == "5":
            from_acc = input("Sender Account Number: ")
            to_acc = input("Receiver Account Number: ")
            amount = float(input("Amount to transfer: "))
            bank.transfer_money(from_acc, to_acc, amount)

        # 6. Barcha accountlar
        elif choice == "6":
            bank.display_accounts()

        # 7. Chiqish
        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid option, try again!")


# --------------------------------------
# RUN PROGRAM
# --------------------------------------
main()





# TASK 2

# --------------------------------------
# POST CLASS
# --------------------------------------
class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def __str__(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nContent: {self.content}\n"


# --------------------------------------
# BLOG CLASS
# --------------------------------------
class Blog:
    def __init__(self):
        self.posts = []

    # 1. Yangi post qo'shish
    def add_post(self, post):
        self.posts.append(post)
        print("Post added successfully!\n")

    # 2. Barcha postlarni ko'rsatish
    def list_all_posts(self):
        if not self.posts:
            print("No posts available.\n")
        else:
            print("\n---- ALL POSTS ----")
            for i, post in enumerate(self.posts):
                print(f"{i}. {post}")

    # 3. Muallif bo‘yicha postlar
    def list_posts_by_author(self, author):
        print(f"\n---- Posts by {author} ----")
        found = False
        for post in self.posts:
            if post.author.lower() == author.lower():
                print(post)
                found = True
        if not found:
            print("No posts by this author.\n")

    # 4. Post o‘chirish
    def delete_post(self, index):
        if 0 <= index < len(self.posts):
            del self.posts[index]
            print("Post deleted successfully!\n")
        else:
            print("Invalid post number!\n")

    # 5. Postni tahrirlash
    def edit_post(self, index, new_title, new_content):
        if 0 <= index < len(self.posts):
            self.posts[index].title = new_title
            self.posts[index].content = new_content
            print("Post edited successfully!\n")
        else:
            print("Invalid post number!\n")

    # 6. Eng so‘nggi postlar
    def latest_posts(self, count=3):
        print("\n---- Latest Posts ----")
        latest = self.posts[-count:]
        if not latest:
            print("No posts yet.\n")
        else:
            for post in reversed(latest):
                print(post)


# --------------------------------------
# MAIN PROGRAM (CLI)
# --------------------------------------
def main():
    blog = Blog()

    while True:
        print("\n--- BLOG MENU ---")
        print("1. Add Post")
        print("2. List All Posts")
        print("3. List Posts by Author")
        print("4. Delete Post")
        print("5. Edit Post")
        print("6. Show Latest Posts")
        print("7. Exit")

        choice = input("Choose an option: ")

        # 1. Add Post
        if choice == "1":
            title = input("Enter Title: ")
            content = input("Enter Content: ")
            author = input("Enter Author: ")
            blog.add_post(Post(title, content, author))

        # 2. List All Posts
        elif choice == "2":
            blog.list_all_posts()

        # 3. List Posts by Author
        elif choice == "3":
            author = input("Author name: ")
            blog.list_posts_by_author(author)

        # 4. Delete Post
        elif choice == "4":
            blog.list_all_posts()
            index = int(input("Enter post number to delete: "))
            blog.delete_post(index)

        # 5. Edit Post
        elif choice == "5":
            blog.list_all_posts()
            index = int(input("Enter post number to edit: "))
            new_title = input("New Title: ")
            new_content = input("New Content: ")
            blog.edit_post(index, new_title, new_content)

        # 6. Latest Posts
        elif choice == "6":
            count = int(input("How many latest posts? "))
            blog.latest_posts(count)

        # 7. Exit
        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid choice, try again!")
            

# --------------------------------------
# RUN PROGRAM
# --------------------------------------
main()





# TASK 3

# --------------------------------------
# ACCOUNT CLASS
# --------------------------------------
class Account:
    def __init__(self, acc_number, holder_name, balance=0):
        self.acc_number = acc_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True
        else:
            return False
    
    def __str__(self):
        return f"Account Number: {self.acc_number}\nHolder: {self.holder_name}\nBalance: {self.balance}\n"


# --------------------------------------
# BANK CLASS
# --------------------------------------
class Bank:
    def __init__(self):
        self.accounts = []

    # Yangi account qo'shish
    def add_account(self, account):
        self.accounts.append(account)
        print("Account added successfully!\n")

    # Accountni raqam orqali topish
    def find_account(self, acc_number):
        for acc in self.accounts:
            if acc.acc_number == acc_number:
                return acc
        return None

    # Balansni ko'rish
    def check_balance(self, acc_number):
        account = self.find_account(acc_number)
        if account:
            print(f"Balance: {account.balance}\n")
        else:
            print("Account not found!\n")

    # Deposit qilish
    def deposit_money(self, acc_number, amount):
        account = self.find_account(acc_number)
        if account:
            account.deposit(amount)
            print("Deposit successful!\n")
        else:
            print("Account not found!\n")

    # Pul yechish
    def withdraw_money(self, acc_number, amount):
        account = self.find_account(acc_number)
        if account:
            if account.withdraw(amount):
                print("Withdrawal successful!\n")
            else:
                print("Insufficient funds! (Overdraft)\n")
        else:
            print("Account not found!\n")

    # Pul o‘tkazish (transfer)
    def transfer_money(self, from_acc, to_acc, amount):
        sender = self.find_account(from_acc)
        receiver = self.find_account(to_acc)

        if sender and receiver:
            if sender.withdraw(amount):
                receiver.deposit(amount)
                print("Transfer successful!\n")
            else:
                print("Insufficient funds! Transfer failed.\n")
        else:
            print("One or both accounts not found!\n")

    # Barcha accountlarni ko'rsatish
    def display_accounts(self):
        print("\n------ ALL ACCOUNTS ------")
        for acc in self.accounts:
            print(acc)


# --------------------------------------
# MAIN PROGRAM (CLI)
# --------------------------------------
def main():
    bank = Bank()

    while True:
        print("\n=== BANK MENU ===")
        print("1. Add Account")
        print("2. Check Balance")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Transfer Money")
        print("6. Display All Accounts")
        print("7. Exit")

        choice = input("Choose an option: ")

        # 1. Account qo'shish
        if choice == "1":
            acc_number = input("Account Number: ")
            holder_name = input("Account Holder Name: ")
            balance = float(input("Initial Balance: "))
            bank.add_account(Account(acc_number, holder_name, balance))

        # 2. Balansni ko‘rish
        elif choice == "2":
            acc_number = input("Enter Account Number: ")
            bank.check_balance(acc_number)

        # 3. Deposit qilish
        elif choice == "3":
            acc_number = input("Enter Account Number: ")
            amount = float(input("Amount to deposit: "))
            bank.deposit_money(acc_number, amount)

        # 4. Pul yechish
        elif choice == "4":
            acc_number = input("Enter Account Number: ")
            amount = float(input("Amount to withdraw: "))
            bank.withdraw_money(acc_number, amount)

        # 5. Pul o‘tkazish (transfer)
        elif choice == "5":
            from_acc = input("Sender Account Number: ")
            to_acc = input("Receiver Account Number: ")
            amount = float(input("Amount to transfer: "))
            bank.transfer_money(from_acc, to_acc, amount)

        # 6. Barcha accountlar
        elif choice == "6":
            bank.display_accounts()

        # 7. Chiqish
        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid option, try again!")


# --------------------------------------
# RUN PROGRAM
# --------------------------------------
main()
