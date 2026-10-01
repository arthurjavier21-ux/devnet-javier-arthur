# Module 1 — Git & GitHub

**Student:** Javier Arthur
**Date:** 10/1/2026

---

## What is Git? What is GitHub? (explain like you're teaching a friend who's never used either)

[Write your own explanation here. What problem does Git actually solve? How is GitHub different from Git itself?]

For me, Git is a tool that helps us keep track sa mga changes na ginagawa natin sa code. Instead na gumawa tayo ng revise file like final1>final2>final2.0, Git can save the history of our changes. So if ever may mali tayong nagawa, pwede natin makita yung previous version and it serves as a guide para ma fix natin.
---

## Key vocabulary (in your own words)

- repository: A repository or repo is like a folder for our project where Git is also tracking the files and changes.
- commit: A commit is like saving a snapshot of my changes. You can also put a message para alam mo kung ano yung ginawa o nabago.
- branch: A branch is like a separate workspace. Dito ako pwede gumawa ng changes without directly changing the main branch.
- push / pull: Push is when you want to send the files to github, while pull is getting the latest content inside the repository.
- pull request: Pull request is a request to add my changes from my branch into the main branch.
- merge conflict: A merge conflict happens kapag may dalawang changes na hindi kayang pagsamahin automatically ni Git.

---

## Walking through what I did

[Describe, step by step, a real branch → commit → push → PR you did. Include the actual commands you used.]

```
git checkout -b midterm
git add .
git commit -m "Modifying Display Menu"
git push -u origin midterm
```

---

## A mistake I made (or one I want to avoid)

[What tripped you up? A confusing error message, committing to the wrong branch, a merge conflict — explain it so a classmate reading this avoids the same mistake.]

Commiting to the wrong branch, minsan nakakalimutan ko kung anong branch ako currently working. Pero pwede nating ma check using git branch, ipapagita neto yung mga branches and kung nassan kang branch currently.

---

## How this connects to something else

[Optional: how does version control relate to anything else you've learned or used before?]
