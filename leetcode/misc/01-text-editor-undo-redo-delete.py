'''
Edge cases

undo() with no history → no-op.
redo() with no future → no-op.
Multiple undo/redo in a row.
append("") or delete(0) → no-op.
Mixed Unicode (works the same in Python strings).
'''

'''
Brute-force idea

Store a full snapshot of the text after every edit in a stack.

append/delete: push the entire string.
undo: pop to previous snapshot; move current to a redo stack.
redo: pop from redo back to current.

Complexity
Time per operation: O(n) (copy whole string of length n).
Space overall: O(total_edits × n) (snapshots are expensive).
'''

'''
OPTIMAL
Keep only the diff needed to reverse an operation:

On append(s): apply it, push ("APPEND", s) to history, clear future.
On delete(k): actually remove the last k chars, push ("DELETE", removed_text) to history, clear future.
undo(): pop from history, apply the inverse to text, push that command to future.
- Undo APPEND s ⇒ delete len(s).
- Undo DELETE t ⇒ append t.
redo(): pop from future, re-apply it, push back to history.

Why it’s good
We store only the exact strings we added or removed.
New edits invalidate the redo stack (standard editor behavior).

Complexity
append(s): O(|s|)
delete(k): O(k)
undo/redo: O(k) where k is the size of the affected text for that command.
Space: O(total_edited_chars) overall (sum of appended/deleted chunks kept once in logs).
'''

from typing import List, Tuple

class TextEditor:
    def __init__(self) -> None:
        # Use list of chars for efficient end-appends/deletes
        self._buf: List[str] = []
        # Stacks of ("APPEND", str) or ("DELETE", str)
        self._history: List[Tuple[str, str]] = []
        self._future: List[Tuple[str, str]] = []

    # ---------- Queries ----------
    def get_text(self) -> str:
        """Return current full text."""
        return "".join(self._buf)

    # ---------- Edits ----------
    def append(self, s: str) -> None:
        """Append s to end. Records diff and clears redo stack."""
        if not s:
            return
        self._buf.extend(s)
        self._history.append(("APPEND", s))
        self._future.clear()  # new edit invalidates redo

    def delete(self, k: int) -> None:
        """Delete last k chars (clamped). Records removed text and clears redo."""
        if k <= 0 or not self._buf:
            return
        k = min(k, len(self._buf))
        # Collect removed text
        removed_chars = self._buf[-k:]
        del self._buf[-k:]
        removed = "".join(removed_chars)
        self._history.append(("DELETE", removed))
        self._future.clear()

    # ---------- Undo/Redo ----------
    def undo(self) -> None:
        """Undo last edit. Moves that edit to the redo stack."""
        if not self._history:
            return
        op, payload = self._history.pop()
        if op == "APPEND":
            # undo append(s): remove len(s)
            to_remove = len(payload)
            if to_remove:
                del self._buf[-to_remove:]
        elif op == "DELETE":
            # undo delete(removed): append removed back
            if payload:
                self._buf.extend(payload)
        self._future.append((op, payload))

    def redo(self) -> None:
        """Redo last undone edit. Moves that edit back to history."""
        if not self._future:
            return
        op, payload = self._future.pop()
        if op == "APPEND":
            if payload:
                self._buf.extend(payload)
        elif op == "DELETE":
            if payload:
                # Delete exactly the same length again
                del self._buf[-len(payload):]
        self._history.append((op, payload))
