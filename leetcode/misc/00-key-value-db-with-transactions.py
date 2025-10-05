'''
# Example 1
kv = TransactionalKVStore()
kv.set("x", 10)
print(kv.get("x"))  # 10

kv.begin()
kv.set("x", 20)
print(kv.get("x"))  # 20
kv.rollback()
print(kv.get("x"))  # 10

kv.begin()
kv.set("x", 30)
kv.commit()
print(kv.get("x"))  # 30


Edge Cases
- Rollback without active transaction → should print "NO TRANSACTION".
- Commit with no transaction → should print "NO TRANSACTION".
- Nested transactions → inner rollback should only undo inner changes.
- Setting a new key inside transaction and rolling back → should remove that key.
- Multiple commits — should persist all changes properly.

Brute force - 
- store multiple copies of dict for all transactions, keep last dict when commiting
- inefficient - unnecessary storage waste
'''

'''
Optimized

get → O(1)
set → O(1) amortized
begin → O(1)
rollback → O(k) (k = keys changed in transaction)
commit → O(1)
Space: O(n + total_keys_modified_in_transactions)

transactions: stack of dicts, each storing old values for keys changed in that transaction.
On set: record old value in top transaction (if not already recorded).
On rollback: revert using top transaction’s change log.
On commit: merge changes into lower transaction or base data.
'''
class TransactionalKVStore:
    def __init__(self):
        self.data = {}              # Main key-value store
        self.transactions = []      # Stack of active transactions (list of dicts)

    def get(self, key):
        """Return current value of a key"""
        return self.data.get(key, None)

    def set(self, key, value):
        """Set key to a value, recording history if in transaction"""
        if self.transactions:
            top = self.transactions[-1]
            # Record previous value only once per transaction
            if key not in top:
                top[key] = self.data.get(key, None)
        self.data[key] = value

    def begin(self):
        """Start a new transaction"""
        self.transactions.append({})

    def rollback(self):
        """Undo changes made in most recent transaction"""
        if not self.transactions:
            print("NO TRANSACTION")
            return
        top = self.transactions.pop()
        for key, old_val in top.items():
            if old_val is None:
                # Key was newly created
                del self.data[key]
            else:
                self.data[key] = old_val

    def commit(self):
        """Persist all open transactions"""
        if not self.transactions:
            print("NO TRANSACTION")
            return
        # Merge all transactions into one final state
        self.transactions.clear()

    def show(self):
        """Debug helper"""
        print("Data:", self.data)
        print("Transactions:", self.transactions)
