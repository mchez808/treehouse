# Exploration Testing

It's about trying out new things in order to find out potential problems.

It sounds less formal and less structured, but it should be added to the test plan.
It's playing around with settings a bit, or parts of app that you'd suspect would have problems.
It's defining what part of the app you want to test, putting any necessary conditions, 
but without exact steps, to figure out what users MIGHT do, before they do it.

Exploration Testing is TIME-BOXED, e.g. 1-2 hours for an app's feature.


# Configuration Testing

Testing out all the systems and their configurations that the software should run on.
This complexity can be well captured in a test matrix documentation.

## Browsers

Example: a UI will depend on the browser, but there's no reason to believe that a REST API will have such dependency.

## Mobile devices

1. Limit scope of which tests are done on all these configurations.  Possibly write mobile-specific tests.

2. Use a VM-based browser testing tool (e.g., CrossBrowserTesting.com or BrowserStack.com)

## Advice for Configuration Testing

Limit testing to more of the bare essentials.

# Acceptance Criteria

We can't test what we don't know!
That's why it's important to ask many clarifying questions and be very specific early on.

Development Process:
Idea -> Feature -> Dev -> Test -> Release

QA is involved in all steps, to avoid huge design and technical challenges at launch.

The solution?  Testing as much as possible.

A system of creating acceptance criteria before anyone starts to code, is of the utmost importance.

In the planning stage, when product managers are introducing the features to the dev team.



# Testing Your Code

The QA Engineer monitors practices and create/enforce processes.


SQA (Software Quality Assurance)

manages the entire development process

SQA is not responsible for directing design and dev fixes.

Quality Control is just one piece of QA.

QA Engineering: coming up with many ways to ensure quality
designing new ways to break the software
discover problems early on in the dev process

Case Study: US Healthcare website, 2013

Key Issues:

* poorly defined requirements

* major software design issues

* not enough testing of entire website start to finish


The QA Engineer:

1. Helps define clear needs that they can test for

2. Helps design the software so that it can be tested

3. Runs all those tests


Testing: the most important aspect of SQA
