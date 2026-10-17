# Guided exercise

**10 minutes of work, then 2 minutes to compare notes.**

## Task

Diagnose the untested edge case and add a test for it, without changing the
mathematical model or the public API.

**Stretch (optional):** replace the slow nested loop and show that the numerical
result is unchanged.

## Before you start (1 minute)

Do the setup in [SETUP.md](SETUP.md) first, then run these from the `psf-demo`
folder with your environment active:

```bash
python check_setup.py   # last line should say "Ready"
python -m pytest        # all tests should pass; note how many
```

If you cloned with Git, put your work on its own branch:

```bash
git status                     # should say "nothing to commit"
git switch -c my-exercise
```

If you used the ZIP, keep an untouched copy of the extracted folder so you can
compare against it.

## Steps

1. Open the `psf-demo` folder in VS Code and open Copilot Chat in **Agent**
   mode, or use your usual AI coding tool. Keep manual approval of edits and
   commands switched on.
2. Open `prompt-template.txt`, fill in the two blanks, and paste the prompt into
   the chat. The README tells you which file holds the model and which command
   runs the tests.
3. Read the plan. Does it want to change anything other than a test file? If
   it does, ask why, or tell it not to.
4. Read each proposed edit before you accept it.
5. Run `python -m pytest` again.
6. Review the whole change: `git diff` in the terminal or the **Source Control**
   view in VS Code. If you used the ZIP, compare the changed file against your
   untouched copy.

## What a good result looks like

- `psf_model.py` is unchanged; only files in `tests/` changed.
- There is a new test whose name says which scientific behaviour it checks,
  with a short comment explaining why the expected value is correct.
- All tests pass, the new one included, and the earlier tests are untouched.
- You can say in one sentence why the expected value in your test is right.

If the agent's test fails, don't loosen the tolerance until it passes.
First decide whether the test or the expectation is wrong.

## Stuck after 4 minutes?

Read the **Sampling and flux** paragraph in `README.md`. Which of its
statements does no existing test check?

## Stretch

Use the stretch version of the prompt at the bottom of `prompt-template.txt`.
A convincing answer keeps the public API unchanged, compares the new
implementation with the original loop on several inputs, and explains why the
chosen tolerance is appropriate. `python analysis.py` prints the run time before
and after the change.

## Windows notes

- Once the environment is active, every command above is the same in
  PowerShell and Command Prompt.
- Paths can be written either way: `python -m pytest tests\test_psf_model.py`
  and `python -m pytest tests/test_psf_model.py` both work.
- `git switch` needs Git 2.23 or newer. Check with `git --version`. Without Git,
  use the ZIP and the untouched-copy approach above.
