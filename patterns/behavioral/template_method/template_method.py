# --- Abstract Class ---

class Cleaner:
    # The template method
    def clean(self):
        success = self.remove_old_entries()
        if success:
            success = self.remove_duplicates()
        return success

    def remove_old_entries(self) -> bool:
        raise NotImplementedError

    def remove_duplicates(self) -> bool:
        raise NotImplementedError


# --- Concrete Class ---

class MongoCleaner(Cleaner):
    def remove_duplicates(self) -> bool:
        print("Removing duplicates in mongo db...")
        return True

    def remove_old_entries(self) -> bool:
        print("Removing old entries in mongo db...")
        return True


class MySQLCleaner(Cleaner):
    def remove_duplicates(self) -> bool:
        print("Removing duplicates in mysql db...")
        return True

    def remove_old_entries(self) -> bool:
        print("Removing old entries in mysql db...")
        return True
