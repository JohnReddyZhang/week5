# Week 5

* Git Internals
* SOLID
* UML
* DDD

References:

* [The Testing Pyramid](http://www.agilenutshell.com/episodes/41-testing-pyramid)
* [Git Book Online](https://git-scm.com/book/en/v2)
* [Learn Git Branching](https://learngitbranching.js.org/)
* [SOLID Ruby Examples](https://rubygarage.org/blog/solid-principles-of-ood)


### Git Cheat Sheet

There are many good cheat sheets online.  

Here are the commands I will demonstrate in class.

* `git init` creates a subfolder named `.git` with initial structure
* `git status`
* `git add` creates new `blob` object
* `git cat-file -p <hash>` to view blob contents
* `git commit` takes snapshot, attaches to timeline, moves `HEAD`
* `git checkout <hash>` syncs working directory, moves `HEAD`
* `git checkout -- <filename>` copies an object into the working directory
* `git branch` lists branches
* `git checkout <branch-name>` moves `HEAD`, syncs working directory

### SOLID

* Single responsibility
* Open for extension, closed for modification
* Liskov substitution
* Interface segregation
* Dependency inversion
