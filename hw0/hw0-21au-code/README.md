# 446-hw-base

The base for CSE 446 homeworks.
This README will be copied for each homework.
Please modify the header for each quarter.

If you are a TA also see [README TA](./README_TA.md).

# Reading Markdown files
Before you start doing anything, please make sure you have a proper way of reading markdown files.
You can use any tool you would like for it.
Python IDEs that we recommend for this class (VSCode or PyCharm) come with Markdown readers built-in.


# Setup

**You only need to do setup once**, then for future homeworks you can run `conda activate cse446`.

## Miniconda installation
Before you start working with this repo, you should install Anaconda.

**Before clicking in the link below** read notes below:

* Linux/Mac OS:
  * If using Linux/Mac please install command line version.
  * Make sure that you choose to initialize conda at startup.
    This will lead to fewer headaches in the future
* Windows:
  * If using Windows, you will need to use Anaconda Terminal, which uses Bash-like syntax.
* Low storage system
  * If you are low of storage (<10GB; for example attu), then Miniconda (see link below) might be a better option.

### Download links

[Anaconda (default)](https://www.anaconda.com/products/individual#Downloads)

[Miniconda](https://docs.conda.io/en/latest/miniconda.html#latest-miniconda-installer-links) (if running low on disk space)

You can find more detailed instructions for installation [at this link](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html#installing-conda-on-a-system-that-has-other-python-installations-or-packages).

## Environment Setup
First make sure you have at least ~5GB of free drive.
From this directory run:
```
conda env create -f environment.yaml
conda activate cse446
pip install -e .
```

First command might take long time. Especially if your connection is slow.

**Then whenever you come back to work on homeworks** just run: `conda activate cse446`

![A quite long gif visualizing how to setup enviornment](./README_media/setup-env.gif)

### Optional - IDE setup

You are welcome to use any IDE as you would like.
Two popular for python are: VSCode (Microsoft) and PyCharm (JetBrains).

#### PyCharm
PyCharm is tailor made for Python, so the setup should be minimal.

Just make sure you point python interpreter to the right path for the project.
To do so, you should follow [these instructions](https://www.jetbrains.com/help/pycharm/configuring-python-interpreter.html#add-existing-interpreter).

Optional: Please note, that to run linting (optional, see below) you will need to use terminal, and run `inv lint`.
You can try setting up linters through *External Programs* section.
If you succeed please let us know, and we will update this section for future reference :D

#### VSCode
VSCode is general purpose IDE, so you will need to install *Python* and *Pylance* extensions (both by Microsoft).


To setup python interpreter, [follow these instructions](https://code.visualstudio.com/docs/python/environments#_select-and-activate-an-environment)
or first reload VSCode, open a folder with homework downloaded and unzipped.
Click into a python file and in bottom left you should see *Python* with some version.
Click into that and choose one that says "cse446".

Now whenever you open terminal it should say "(cse446)" on the left hand side,
and `which python` should also output path with `cse446` in it.
Sometimes, it doesn't work with the first terminal after VSCode opens, so `exit` it and reopen it (Ctrl+J).

Optional: For linting you will need to *enable* flake8, mypy and *disable* pylint.
Rather than following the official guide, press (Ctrl/Cmd + Shift + P), select "Preferences: Open Workspace Settings" or "Preferences: Open User Settings", in search type "flake8", "mypy" and "pylint".
Each should have an option called "Python > Linting: -linter- Enabled" which you should toggle *on* for flake8 and mypy and toggle *off* for pylint.

Extra Optional: Extensions for VSCode and quite helpful apart from support for specific language. I highly recommend downloading Trailing Spaces by Shardul Mahadik and Visual Studio IntelliCode by Microsoft.
Also if you are advanced LaTeX user there is LaTeX Workshop by James Yu and LaTeX Utilities by tecosaur.
These require you to download and install LaTeX manually though.

# Usage

## Submission

When you are done with coding run.
```
inv submit <hw-number (i.e. 0, 1, 2, ...)>
```
this will generate a `.zip` file that should be uploaded to gradescope for automated grading.

For example running:
```
inv submit 1
```
will result in `submission_hw1.zip` generated, which should be submitted under HW1 coding assignment on gradescope.

![gif visualizing submission process](./README_media/submit.gif)


## Testing
In this class we will use unittest framework in python to automatically grade coding problems.
Some of the tests are provided to you, so that you can validate your results.

To run tests:
```
inv test
```

The output should look something like this:
```
> inv test
FFF..
======================================================================
FAIL: test_polyfeatures_fives (public.poly_regression.test_poly_regression.TestPolyReg)
----------------------------------------------------------------------
Traceback (most recent call last):
  File ...
AssertionError: 
Arrays are not almost equal to 6 decimals

(shapes (1,), (20, 1) mismatch)
 x: array([1.])
 y: array([[5.],
       [5.],
       [5.],...
```

You can see that in the top there are 3 `F`'s and 2 `.`'s. `F`'s correspond to failed tests and `.` correspond to correct tests.

There are few things to note:

- Not all tests are equal. Some are worth more points. This will not be displayed when you run `inv test`.
- We **do not** provide you with all tests. There are many that hidden. Even if you pass all *public* tests you may still fail some *hidden* ones.

## Linting

Linting is **not required** for this class.
However, we recommend that you keep your code linted.
Especially if this is your first time learning python, or if you never had a formal introduction.

For this we provided you with a simple script to track issues & possibly fix your code.
To run linter:
```
inv lint
```
which will generate output
```
> inv lint
flake8 homeworks
homeworks/hw1/poly_regression/polyreg.py:103:5: E303 too many blank lines (4)
```
You can see that issue points to file (`polyreg.py`), line (105) and column (3) as well as the issue "too many blank lines".

Note that we are using 4 linters (flake8, isort, black, mypy; in that order).
If you have issues that are pointed out by isort or black you can run `inv lint --apply` to automatically apply fixes.

Again, linting is **not required** for this class.
If you don't want to lint your code, or prefer some other linting setup that's ok.