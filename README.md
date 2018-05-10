# TRANSPOSE journal policies database

[![Build Status](https://travis-ci.com/transpose-publishing/policies-database.svg?branch=master)](https://travis-ci.com/transpose-publishing/policies-database)

We're crowd-sourcing a database of journal policies relating to peer review (openness, recognition for co-reviewing) and preprinting.

### Why TRANSPOSE?

While there are fantastic databases that indicate whether archiving a preprint is allowed ([Sherpa/RoMEO](http://www.sherpa.ac.uk/romeo/search.php)) and whether journals are partnered with [Publons](https://publons.com/journal/?order_by=reviews), to our knowledge, there is no database of information on topics such as:
- the openness of peer review (whether the content of peer reviews and the identities of reviewers are published, or whether reviews can be transferred to other journals), 
- recognition for peer review (whether postdoc co-reviewers are acknowledged), 
- _detailed_ policies on preprinting (for example, what version is ok to post, whether preprints can be cited, and what licenses and media coverage of preprints are permitted).

Without this kind of information, it's difficult to monitor or advocate for changes that would make scholarly publishing more open and fair. It's also difficult for authors to easily compare different journals to make choices that support their needs and interests in open communication.

In order to address this, we're building a user-editable database that contains this information. The database entries are human-readable YAML files that we'll use to build visualizations on the web down the road.

For more information on this initiative, visit our [homepage](http://transpose-publishing.github.io).

## Contributing

We welcome contributions! See our [contribution guidelines](CONTRIBUTING.md) to get started.

## Participation Guidelines

This project adheres to a [code of conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code. Please report unacceptable behavior to jessica.polka@asapbio.org.

## MozSprint

Join us at the [Mozilla's Global Sprint](http://mzl.la/global-sprint/) May 10-11, 2018! We'll be gathering in-person at sites around the world and online to collaborate on this project and learn from each other. [Get your #mozsprint tickets now](http://mzl.la/global-sprint/)!
- Find issues we're looking for help with labeled "mozsprint" [here](https://github.com/transpose-publishing/policies-database/issues)
- TRANSPOSE on the Mozilla Global Sprint repo [here](https://github.com/mozilla/global-sprint/issues/269)
- We discussed the TRANSPOSE project on a Mozilla Sprint Demo call at 12pm ET (16:00 UTC) on Tuesday, May 8, 2018. [See notes and join info](https://public.etherpad-mozilla.org/p/ol5-demos-b)
- During the Sprint, we can keep in touch via Gitter: [![Gitter chat](https://badges.gitter.im/gitterHQ/gitter.png)](https://gitter.im/transpose-publishing/Lobby#)
- Jessica will be working on this project from the Boston site

![Global Sprint](https://user-images.githubusercontent.com/617994/37716586-3b0397a0-2cf5-11e8-8c6f-bad01f67f50e.jpg)

## Local usage

Most users will not need to run the code in this repository locally.
However, if you'd like to modify the code or test a change locally, follow these instructions.

This repository uses [conda](http://conda.pydata.org/docs/) to manage its environment as specified in [`environment.yml`](environment.yml).
Install the environment with:

```sh
conda env create --file=environment.yml
```

Then use `conda activate policies-database` and `conda deactivate` to activate or deactivate the environment.

With the environment activated, you can validate YAML policy files with the following commands:

```sh
# Validate a single test YAML policies
pykwalify \
  --data-file policies/test-policies/test-policy-id-only.yml \
  --schema-file policies/schema.yml

# Validate all YAML files in policies/policies
pytest policies/validate_policies.py
```

## License

All original work in this repository is dedicated to the public domain under the CC0 license.
See [LICENSE.md](LICENSE.md).
SHERPA RoMEO data is reused under its CC BY-NC-SA 2.5 License.
Learn more in the [`romeo`](romeo) README.
