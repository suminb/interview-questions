# Interview Questions

Job interviews sometimes can be a daunting task. Especially when you're
confronted with those algorithm and data structure problems.

I'm sure you've been through a lot when you were in school. Linked lists,
binary trees, directed graphs, hash maps, greedy algorithm, divide and conqure,
dynamic programming, depth first search, breath first search and all those good
stuff. You were also getting the hang of space and time complexity analysis.

Although computer science classes were pain in the \*\*\*, you finally
graduated. You will remember all those all-nighter days with your classmates
trying to build a compiler, a file system, and a network router. You realized
you can push yourself much further than you thought possible. Even with years
of hard work, you probably wouldn't claim that you have conquered the universe
of computer science, because you know there is much more to be learned, but at
least you had some level of confidence that you understand the fundamentals.

You got a job as a software engineer. You started building awesome stuff.
Years have passed by, and things got rusty. Even though you were writing some
code pretty much every single day, you weren't always concerned with
implementing algorithms yourself. In many cases, you were working on the top of
some libraries and frameworks to get things done.

Then here we go. You made all the way through the final round of your hiring
process and you were invited to an on-site interview. You are standing in front
of a big whiteboard. Your interviewer is asking you to write some code to merge
two lists of sorted intergers. It is supposed to be an *easy* problem, but
writing code on a whiteboard without syntax highlighting, without
auto-complete, without any compiler or interpreter is a completely different
experience when compared to writing code at your regular daily job.

<a href="https://imgflip.com/i/2cuu5x"><img src="https://i.imgflip.com/2cuu5x.jpg" title="made at imgflip.com"/></a>

I recently had a number of job interviews with different companies. Some
interviews went well, others were a bit more challenging than they are supposed
to be. I've got a few offers and one rejection so far. Some are still
in-progress and one of them is highly likely going to turn out as a rejection.

I was very lucky that one of the companies that I had an interview with gave me
detailed feedback. They shared comments from each of four interviewers, which
is very unusual. In essence, they had positive evaluation on the behavioral
interview (communication skills, personality, cultural fit, leadership, etc.)
and the system design interview (designing scalable systems at extreme sizes),
but they had some doubts about my coding abilities. Regardless of the outcome,
I sincerely appreciate that kind of feedback. That's what keeps me moving
forward.

It's okay to fail. It's okay to make mistakes. As [Dr.
Hong](http://www.romela.org/dr-dennis-hong/) said, *you can't always win, but
you can always learn*. I've created this repository in an attempt to *learn
from mistakes*.


## This Repository

This repository contains some on-site interview questions that I have
encountered over the course of last few  years. I'm still working on providing
solutions for some of the problems. No particular company name is mentioned,
but those questions are general enough that they can be asked in any tech
interview.


## Practice

Try to focus on these two things:

Getting a complete, working solution is important. Pseudo-code is not enough.
Interviewers are generally okay with any language of your choice among popular
ones (C/C++, Java, Python, etc.) but I'd avoid using bizarre languages like
[Whitespace](https://en.wikipedia.org/wiki/Whitespace_(programming_language)),
[Brainfuck](https://en.wikipedia.org/wiki/Brainfuck), or
[아희](https://aheui.github.io/specification.en). No matter what language you
use, practice to get *working* code with some time limit. Try to get all the
boundary conditions right.

You are generally expected to write code on a whiteboard or on a basic text
editor without syntax highlighting. You should be able to run the code in your
head comfortably. It may be acceptable to write some fuzzy code that partially
works then gradually improve by running the code with a compiler or an
interpreter in a real work environment. But that is not how things work at a
job interview. Try to write code at the entirety, improve the code if possible,
simulate all possible edge cases, fix any bug you found. When you think all is
good, run your code to see if your code really works.


## Time Limits

In many cases, a final round consists of multiple interview sessions. The
longest one I have had so far was five sessions long. Each interview session
runs for about 50-60 minutes. Generally, you and your interviewer will spend
some time introducing yourself, with regards to your current role and your past
experience, to the other and vice versa. Your interviewer may ask you some
behavioral questions. Most interviewers want to leave a few minutes at the end
of the session for you to ask some questions. That leaves about 30-40 minutes
at most for the coding part itself.

For each problem description, I wrote down how much time I had for that
particular problem.


## Contribution

Feel free to submit your solutions via pull requests. Some rules to follow:

- Your solution must be contained in a single file.
- Avoid relying on external libraries and frameworks.
- File name should be in a format of `solution-{your GitHub username}.{ext}`.
  For example, if your GitHub username is `johndoe` and your solution is
  written in C++, your filename should be `solution-johndoe.cpp`
