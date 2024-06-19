# Instructions

### Installation Steps

You will need to follow steps below to install required components and run tests


- Download and install Python and Git to your machine
- Clone the repository

  `git clone https://github.com/PetricaStoica/NewswireTestAutomation.git`

- Install required packages

  ``` shell
  cd NewswireTestAutomation
  python -m pip install -r requirements.txt
  ```

  
- Run `pytest -s`

- On the Captcha step, the tests will display this message in the console 'Have you manually completed the CAPTCHA challenge? (confirm with: y)'

The user should manually complete the Captcha challenge and click Verify in the Captcha form, then type y and Enter in the console

- From this point the tests will execute and should return a ==== 2 passed in 40.36s ===== result
