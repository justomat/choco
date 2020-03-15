# zacc

zacc keeps teams accountable for their tech-debts.

#### bash one-liner
```bash
git grep -n TODO | awk '{split($1,arr,":"); print "git blame -f -n -L"  arr[2] "," arr[2], arr[1] }' | parallel
```
