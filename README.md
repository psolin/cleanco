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
Download it from this site and unzip the directory.

* Mac: `cd` into it, and enter `sudo python setup.py install` along with your system password.
* Windows: Same thing but without `sudo`.

## How does it work?
Let's look at some sample code.  First, create an instance of the module:

    >>> from cleanco import cleanco

Prepare a string of a company name that you want to process:

    >>> business_name = "Some Big Pharma, LLC"

Throw it into the instance:

    >>> x = cleanco(business_name)

You can now get the company types:

    >>> x.type()
    ['Limited Liability Company']

...the possible countries...

    >>> x.country()
    ['United States of America', 'Philippines']

...and a clean version of the company name.

    >>> x.clean_name()
    'Some Big Pharma'

## Are there bugs?
You better believe it.  Please let me know or fork this project.  I'm sure some of the company suffixes are way incorrect and I'm missing a lot more information.

## Special thanks to:

- Wikipedia's [Types of Business Entity article](http://en.wikipedia.org/wiki/Types_of_business_entity), where I spent hours of research.
- Contributors: Petri Savolainen <petri.savolainen@koodaamo.fi>
