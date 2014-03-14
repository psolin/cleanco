#cleanco

## What is it / what does it do?
This is a Python module that processes company names.

## How do I install it?
Download it from this site and unzip the directory.

* Mac: `cd` into it, and enter `sudo python setup.py install` along with your system password.
* Windows: Same thing but without `sudo`.
* Linux: ???

There may also be a way to do `pip install` but I can't guarantee this.

## How does the module work?
Let's look at some sample code.  First, initialize the module:

    >>> from cleanco import cleanco

Now, come up with a company name that you want to process:

    >>> companyname = "Paul Pharmaceutical, Inc."

Throw it into the module:

    >>> processing = cleanco(companyname)

You can now get the company types:

    >>> cotype = processing.type()
    >>> print cotype
    ['Corporation']

...the possible countries...

    >>> country = processing.country()
    >>> print country
    ['Philippines', 'United States']

...the possible industries...

    >>> industry = processing.industry()
    >>> print industry
    ['Pharmaceutical']

...and a clean version of the company name.

    >>> clean = processing.cleanname()
    >>> print clean
    Paul Pharmaceutical

There is also a short version of the company name for times when you want to remove things in parenthesis or everything after a hyphen.  You can access this with `.shortname()`.

## Are there bugs?
You better believe it.  Please let me know or fork this project.  I'm sure some of the company suffixes are way incorrect and I'm missing a lot more information.

## Special thanks to:
Wikipedia's [Types of Business Entity article](http://en.wikipedia.org/wiki/Types_of_business_entity), where I spent hours of research.