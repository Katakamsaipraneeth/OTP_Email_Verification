Project Objective:
--------------------
To ensure secure user verification by sending a randomly generated OTP (One-Time Password) directly to a user’s email.

Key Features:
---------------
*Random OTP Generation: Generates a unique 4-digit OTP to ensure secure access.
*Email Integration with Gmail SMTP: Uses Python’s smtplib library to send OTPs seamlessly via email.
*Secure Authentication: Stores email credentials in environment variables, keeping sensitive information safe.
*User Verification Prompt: Requests users to input the OTP received, validating their identity.
*Error Handling: Catches and manages errors for a smooth user experience.

Technologies Used:
-------------------------
. Python (Core functionality)
. SMTP (Email communication)
. Environment Variables (For credential security)

