#cleanco - 1.0

## What is it / what does it do?
This is a Python module that processes company names, in terms of US/UK business entity types.

## How do I install it?
Download it from this site and unzip the directory.

* Mac: `cd` into it, and enter `sudo python setup.py install` along with your system password.
* Windows: Same thing but without `sudo`.

## How does the module work?
Let's look at some sample code.  First, initialize the module:

    >>> from cleanco import cleanco

Now, come up with a company name that you want to process:

    >>> business_name = "Some Big Pharma, LLC"

Throw it into the module:

    >>> processing = cleanco(business_name)
    >>> x = processing.cleaner()

You can now get the company types:

    >>> x.type
    ['Limited Liability Company']

...the possible countries...

    >>> x.country
    ['United States of America', 'Philippines']

...the possible industries...

    >>> x.industry
    ['Pharmaceutical']

...and a clean version of the company name.

    >>> x.clean_name
    'Some Big Pharma'

## Are there bugs?
You better believe it.  Please let me know or fork this project.  I'm sure some of the company suffixes are way incorrect and I'm missing a lot more information.

## Special thanks to:
Wikipedia's [Types of Business Entity article](http://en.wikipedia.org/wiki/Types_of_business_entity), where I spent hours of research.
