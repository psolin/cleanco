# cleanco - clean organization names

## What is it / what does it do?

This is a Python package that processes company names, providing cleaned versions of the
names by stripping away terms indicating organization type (such as "Ltd." or "Corp").

Using a database of organization type terms, It also provides an utility to deduce the
type of organization, in terms of US/UK business entity types (ie. "limited liability
company" or "non-profit").

Finally, the system uses the term information to suggest countries the organization could
be established in. For example, the term "Oy" in company name suggests it is established
in Finland, whereas "Ltd" in company name could mean UK, US or a number of other
countries.

## How do I install it?
Just use 'pip install cleanco' if you have pip installed (as most systems do). Or download the zip distribution from this site, unzip it and then:

* Mac: `cd` into it, and enter `sudo python3 setup.py install` along with your system password.
* Windows: `python setup.py install`.

## How does it work?
If you only want a clean version of the company name, first pull in the terms:

    >>> terms = get_terms()

Then, run the string and the terms through the "basename" function:

    >>> basename("Daddy & Sons, Ltd.", terms)
    Daddy & Sons

If you want to classify the name by business entity type, first select it as a source:

    >>> classification_sources = typesources()

Then, run the string and classication source through the "matches" function:

    >>> matches("MyCompany Ltd", classification_sources)
    ['Limited']

If you want to classify the name by possible countries, first select it as a source:

    >>> classification_sources = countrysources()

Then, run the string and classication source through the "matches" function:

    >>> matches("MyCompany Ltd", classification_sources)
    ['United States of America', 'Philippines']

## Compatibility with previous versions
cleanco's API was simplified in version 2.0. While previous functions are still compatible, they are not preferred.

## Are there bugs?
See the issue tracker. If you find a bug or have enhancement suggestion or question, please file an issue and provide a PR if you can. For example, some of the company suffixes may be incorrect or there may be suffixes missing.

To run tests, simply install the package and run `python setup.py test`. To run tests on multiple Python versions, install `tox` and run it (see the provided tox.ini).

## Special thanks to:

- Wikipedia's [Types of Business Entity article](http://en.wikipedia.org/wiki/Types_of_business_entity).
- Contributors: Petri Savolainen <petri.savolainen@koodaamo.fi>
