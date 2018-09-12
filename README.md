# Amazon MasterCard CSV Statement Converter #
The [New Day portal][new-day] lets you export your Amazon MasterCard statement as a CSV file. Unfortunately, the format used is incompatible with [FreeAgent][freeagent].

[new-day]: https://portal.newdaycards.com/amazon/login
[freeagent]: https://freeagent.com

This script fixes that problem.

## Usage ##
If you use [Pipenv][pipenv], here's how to install the dependencies, and run the script:

[pipenv]: https://pipenv.readthedocs.io/en/latest/

```python
$ cd /path/to/project
$ pipenv install
$ pipenv run ./fix.py path/to/input.csv path/to/output.csv
```

If you don't use Pipenv, you're on your own. Honestly, you're on your own anyway; I have no interest in making this my life's work.

## Caveats and disclaimers ##
This is a _very_ basic script, with no error checking whatsoever. Misuse may result in embarrassment, injury, or death. Exercise caution before using.