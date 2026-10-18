# Keep evidence specialists read-only

Keep Explorer and Librarian read-only so they stay focused on evidence gathering rather than take on implementation work suited to Junior. They may use temporary research files and caches, but must not change the repositories or user files they investigate.

Read-only inspection may cause incidental internal maintenance, such as `git status` updating Git's index. This does not authorize edits or builds.

Shell-command safety checks must account for incidental maintenance: treating every hidden write as disallowed would reject ordinary inspection such as `git status`.
