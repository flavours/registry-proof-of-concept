
# Flavour registry - Proof-Of-Concept

Warning: As stated, this is just a proof of concept and the behavior will change in the future.


# Get your own copy

This is still a proof of concept. 

 * Create a new project on divio cloud but dont deploy it! The project should be using "python 3.6" and be a plain "django" project.
 * Check it out locally using the divio cli: `divio project setup <PROJECT_SLUG>` and `cd <PROJECT_SLUG>`
 * Add the registry upstream repository to your checkout: `git remote add upstream git@github.com:flavours/registry-proof-of-concept.git`
 * Fetch from upstream: `git fetch upstream`
 * Force reset master to the new remote origin master: `git reset --hard upstream/master`
 * Push the new branch to divio: `git push -f origin master`
 * Deploy on the test environment and see if everything works!

 ## Keep it updated

 * Change into the project if you have not already
 * Pull from new remote: `git fetch upstream`
 * Merge all changes: `git merge upstream/master`
 * Push back: `git push origin master`. A force push should not be required.

# Todo

* user management and authentication
* shared namespace management
* API tokens
* CRUD API for addons and addon versions

# Changelog

## 0.1 (20-9-2019)

* initial
