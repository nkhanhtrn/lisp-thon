# Lisp Interpreter in Python

This is a fun take to learn how interpreter works by building a simple (yet functional) Lisp interpreter.

## How to use

- `python lisp-thon` and the `eval > ` console will apprear

## Supported features

- Small set of Scheme
- All math operators
- Lambda & local scope

## How it works

Lisp Interpreter (or most interpreter) works by doing the following tasks:

- Parse source code into Abstract Syntax Tree: In this version, AST is represented under nested list. For example:
`(print (* pi ( * r r))` equals `[print, [ *, pi, [ *, r, r]]]`
- Travel the tree using in-order traversal
- `eval` the source code and return correct evaluated values
