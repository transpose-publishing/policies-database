# Contributing to TRANSPOSE

Thanks so much for your interest in contributing to TRANSPOSE!

Peer review is foundational to our current system of creating and sharing knowledge, yet almost everything about this process is typically shrouded in secrecy. In order to make the publishing process more open, accessible, and fair, we will work to bring transparency to journal policies and practices, about which little is known on a systemic level. To accomplish this, we'll build a user-editable database of journal policies on the openness of peer review, the recognition of early career researchers who contribute to peer review, and detailed policies on preprinting. To accomplish this, we'll build off of the [SHERPA/RoMEO database](http://www.sherpa.ac.uk/romeo/index.php), which contains information about preprint archiving and also an ontology of journals, publishers, and policy groups.

These guidelines will help you get involved with TRANSPOSE.

* [Participation guidelines](#participation-guidelines)
* [What we're working on](#what-were-working-on)
* [How to change policy records](#how-to-change-policy-records)
* [How to report bugs](#how-to-report-bugs)
* [Communication channels](#communication-channels)

## Participation guidelines

This project adheres to a [code of conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code. Please report unacceptable behavior to jessica.polka@asapbio.org.

## What we're working on

Check the [issue tracker for projects labeled MozSprint!](https://github.com/transpose-publishing/policies-database/issues?q=is%3Aopen+is%3Aissue+label%3Amozsprint)

Specifically, we'd like to begin filling in information relevant to some of the largest or most prominent journals. Check this list of [prioritized journals](https://github.com/transpose-publishing/policies-database/issues/4) and find one you'd like to work on.

## How to change policy records

You can change policy entries in just a few minutes in your browser!

1. **Fork the repo.** Press the "Fork" button at the top right of the screen to fork this repository to your own account. (You only need to do this once)
2. **Identify a policy you want to edit.** In [transpose-publishing/policies-database](https://github.com/transpose-publishing/policies-database), search for your journal name of choice in the search bar at the top of the screen. If the journal appears in a policy record, you will see a file like "/policies/romeo_4.yml" show up in the search results. Copy this file path.
3. **Find the policy in your own fork.** In your own fork of the repository, press "find file" (next to the green "Clone or Download" button). Now paste the file path from the previous step here.
4. **Edit the record.** Once you're looking at a policy record, click the pencil icon to edit it. Fill in as much information as you would like by referencing the journal website. Please also add references for the information you're adding in the corresponding url fields. Many journals won't have explicit policies on the web, so don't worry about filling out everything! Tips for editing: If you're pasting long text in, keep everything on the same line. Leave one space betwen the colon in the data field and your response, like so:
```yaml
open-reports: yes
```

5. **Commit changes.** Press the green "Commit changes" button at the bottom of the page to save your edits to your own copy of the repository. At this point, you can repeat steps 2-6 if you want to change more policies!
6. **Submit a pull request.** To propose merging your changes back into the master copy, navigate back to [transpose-publishing/policies-database](https://github.com/transpose-publishing/policies-database). Click the "New pull request" button. On the next screen, click the text link that says "Compare across forks" and change the "Head fork" drop down to your own copy of the repo. Then click the green "Create pull request" button.
7. That's it! We'll leave a comment if we notice any issues or problems that could be revised.

More general information about this process is below:
 
1. **[Fork](https://help.github.com/articles/fork-a-repo/) this repository**. This makes your own version of this project you can edit and use.
2. **[Make your changes](https://guides.github.com/activities/forking/#making-changes)**! You can do this in the GitHub interface on your own local machine. Once you're happy with your changes...
3. **Submit a [pull request](https://help.github.com/articles/proposing-changes-to-a-project-with-pull-requests/)**. This opens a discussion around your project and lets the project lead know you are proposing changes.

First time contributing to open source? Check out this *free* series, [How to Contribute to an Open Source Project on GitHub](https://egghead.io/series/how-to-contribute-to-an-open-source-project-on-github).

## How to report bugs

Notice a mistake? Please file any bugs, requests, or questions in our [issue tracker](https://github.com/transpose-publishing/policies-database/issues)!

## Communication channels

[![Gitter chat](https://badges.gitter.im/gitterHQ/gitter.png)](https://gitter.im/transpose-publishing/Lobby#)
