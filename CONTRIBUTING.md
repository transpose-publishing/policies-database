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

You can change policy entries in just a few minutes in your browser! To get started, you'll need a GitHub account (click on "Sign up" in the top right of your screen to make one - don't forget to verify your account by clicking on the link in the confirmation email!)

### Step 1: Locating the journal policy
Using the search bar at the top of the screen, type in your journal name of choice, ideally enclosed in quotes. (If you're looking for inspiration, try our list of [prioritized journals!](https://github.com/transpose-publishing/policies-database/issues/4)) If the journal is in the database, you will see a link to a file such as "policies/policies/romeo_201.yml. Click it to look at the policy record. 

_Notice that there can be multiple journals associated with a policy record, and publishers can have their journals divided into one or more policy groups (for example, Cell Press has policies that are different from its parent, Elsevier). These relationships are derived from SHERPA/RoMEO ontology._

![tutorial1](https://github.com/transpose-publishing/policies-database/blob/master/media/tutorial1anno.PNG)

### Step 2: Initiating the edit
Using the drop-down menu at left, make sure you're looking at the master branch. Next, click the pencil icon at right.

![tutorial2](https://github.com/transpose-publishing/policies-database/blob/master/media/tutorial2anno.PNG)

### Step 3: Editing the file
Now add information about the relevant policy, using the journal or publisher website as your reference! Please:
- Leave one space between a property and the value you enter there, eg ```open-reports: yes```
- For every policy you enter, please add a reference url to the corresponding field
- Please enter only the values suggested
- If you notice that not all the journals listed at the top of the file share the same policy, please leave a note in the ``flag-romeo`` field.

When you're finished, enter a short description of what you did in the box at the bottom of the page and click the green "Propose file change" button. 

![tutorial3](https://github.com/transpose-publishing/policies-database/blob/master/media/tutorial3anno.PNG)

### Step 4: Create a pull request
On the next screen, press the green "Create pull request" button...

![tutorial4](https://github.com/transpose-publishing/policies-database/blob/master/media/tutorial4anno.PNG)

...and do the same once more on the final page.

![tutorial5](https://github.com/transpose-publishing/policies-database/blob/master/media/tutorial5anno.PNG)

That's it! A member of the TRANSPOSE team will review your pull request and make sure it's ready to merge into the master branch. If there's a problem, we'll get in touch - but otherwise, you're done! You can repeat this process for every policy entry you would like to change.


## How to report bugs

Notice a mistake? Please file any bugs, requests, or questions in our [issue tracker](https://github.com/transpose-publishing/policies-database/issues)!

## Communication channels

[![Gitter chat](https://badges.gitter.im/gitterHQ/gitter.png)](https://gitter.im/transpose-publishing/Lobby#)

## Data source
[![Sherpa Romeo](https://github.com/transpose-publishing/transpose-publishing.github.io/blob/master/images/romeosmall.gif)](http://www.sherpa.ac.uk/RoMEO.php)

Information in the policy records is derived from the RoMEO database which is compiled by SHERPA and has been modified for use here. Data from SHERPA RoMEO is licensed under a [Creative Commons Attribution-NonCommercial-ShareAlike 2.5 License.](https://creativecommons.org/licenses/by-nc-sa/2.5/)

_Note that as per our [LICENSE](LICENSE.md), all original contributions will be licensed CC0!_
