# ben-tools

This tool is designed to add contacts into an automation using the automation id and the subscriber id's of all of the contacts.

Some use case examples:
  1. You need to add contacts to an automation but there is no valid segment that contains all those contacts
  2. You are adding a large number of contacts to an automation that may time out when using the Bulk Edit tool
  
*Before going further make sure you have pipenv or homebrew installed.*
  
**Getting started**
  1. Clone this repository
  2. Run 'pipenv install' in the terminal for this directory
  3. Gather a list of all of the contact ids
  4. Get the series id
  5. Find the client's API key and API URL
  
**Running the tool**
  1. Open the file addToAutomation.py
  2. Add the information you gathered from the getting started section to the appropriate sections
  3. Save the file
  4. In the terminal at the root of the directory run 'python addToAutomation.py'
  5. The tool should start printing the status codes and subscriber id to the terminal as they are processed
  6. Once the contacts have been processed a list of ids for the failed attempts is printed
  
**Manual testing**
  1. Follow the steps for the *Running the tool* section using a single contact in a test account
  
**Notes**
  1. Do not commit API keys to github!!!!!!!!
  2. See step 1
  3. Ideally you should not commit anything for this tool
  
Please contact me with any questions
