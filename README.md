# cleanco - clean organization names

![Python package](https://github.com/psolin/cleanco/workflows/Python%20package/badge.svg)
![CodeQL](https://github.com/psolin/cleanco/workflows/CodeQL/badge.svg)

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

* Mac: `cd` into it, and enter `sudo python setup.py install` along with your system password.
* Windows: Same thing but without `sudo`.

## How does it work?
Let's look at some sample code. To get the base name of a business without legal suffix:

    >>> from cleanco import basename
    >>> business_name = "Some Big Pharma, LLC"
    >>> basename(business_name)
    >>> 'Some Big Pharma'

Note that sometimes a name may have e.g. two different suffixes after one another. The cleanco
term data covers many of these, but you may want to run `basename()` twice on the name, just in case.

If you want to use your custom terms, please see  `custom_basename()` that also provides some other ways to adjust how base name is produced.

To get the business type or country:

    >>> from cleanco import typesources, matches
    >>> classification_sources = typesources()
    >>> matches("Some Big Pharma, LLC", classification_sources)
    ['Limited Liability Company']

To get the possible countries of jurisdiction:

    >>> from cleanco import countrysources, matches
    >>> classification_sources = countrysources()
    >>> matches("Some Big Pharma, LLC", classification_sources) ´
    ['United States of America', 'Philippines']


## Are there bugs?
See the issue tracker. If you find a bug or have enhancement suggestion or question, please file an issue and provide a PR if you can. For example, some of the company suffixes may be incorrect or there may be suffixes missing.

To run tests, simply install the package and run `python setup.py test`. To run tests on multiple Python versions, install `tox` and run it (see the provided tox.ini).

## Special thanks to:

- Wikipedia's [Types of Business Entity article](http://en.wikipedia.org/wiki/Types_of_business_entity), where I spent hours of research.
- Contributors: [Petri Savolainen](https://github.com/petri)
