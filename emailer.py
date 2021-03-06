import smtplib
import os
from email.message import EmailMessage

#   html for successfull registration t=1
#   html for deregistering t=2
# ? html for announcement ?t=3

f = open("atreides.txt", "r")
a = (f.readlines())
f.close()

EMAIL_ADDRESS = str(a[0])
EMAIL_PASSWORD = str(a[1])


def temp_1(rec, subject):

    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = "PyBot(do-not-reply)"
    msg["To"] = str(rec)

    msg.set_content("Do not reply to this email")

    msg.add_alternative(
        """<!DOCTYPE html>
<html>
  <head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <title>Automated Reply from PyBot</title>
    <style>
      @media only screen and (max-width: 620px) {
        table.body h1 {
          font-size: 28px !important;
          margin-bottom: 10px !important;
        }

        table.body p,
        table.body ul,
        table.body ol,
        table.body td,
        table.body span,
        table.body a {
          font-size: 16px !important;
        }

        table.body .wrapper,
        table.body .article {
          padding: 10px !important;
        }

        table.body .content {
          padding: 0 !important;
        }

        table.body .container {
          padding: 0 !important;
          width: 100% !important;
        }

        table.body .main {
          border-left-width: 0 !important;
          border-radius: 0 !important;
          border-right-width: 0 !important;
        }

        table.body .btn table {
          width: 100% !important;
        }

        table.body .btn a {
          width: 100% !important;
        }

        table.body .img-responsive {
          height: auto !important;
          max-width: 100% !important;
          width: auto !important;
        }
      }
      @media all {
        .ExternalClass {
          width: 100%;
        }

        .ExternalClass,
        .ExternalClass p,
        .ExternalClass span,
        .ExternalClass font,
        .ExternalClass td,
        .ExternalClass div {
          line-height: 100%;
        }

        .apple-link a {
          color: inherit !important;
          font-family: inherit !important;
          font-size: inherit !important;
          font-weight: inherit !important;
          line-height: inherit !important;
          text-decoration: none !important;
        }

        # MessageViewBody a {
          color: inherit;
          text-decoration: none;
          font-size: inherit;
          font-family: inherit;
          font-weight: inherit;
          line-height: inherit;
        }

        .btn-primary table td:hover {
          background-color: #34495e !important;
        }

        .btn-primary a:hover {
          background-color: #3455db !important;
          border-color: #3455db !important;
        }
        .btnhr a:hover {
          background-color: #14b353 !important;
          border-color: #14b353 !important;
        }
        .btncd a:hover {
          background-color: #4d4d4d !important;
          border-color: #4d4d4d !important;
        }
      }
    </style>
  </head>
  <body
    class=""
    style="
      background-color: #f6f6f6;
      font-family: sans-serif;
      -webkit-font-smoothing: antialiased;
      font-size: 14px;
      line-height: 1.4;
      margin: 0;
      padding: 0;
      -ms-text-size-adjust: 100%;
      -webkit-text-size-adjust: 100%;
    "
  >
    <span
      class="preheader"
      style="
        color: transparent;
        display: none;
        height: 0;
        max-height: 0;
        max-width: 0;
        opacity: 0;
        overflow: hidden;
        mso-hide: all;
        visibility: hidden;
        width: 0;
      "
      >You have registered successfully</span
    >
    <table
      role="presentation"
      border="0"
      cellpadding="0"
      cellspacing="0"
      class="body"
      style="
        border-collapse: separate;
        mso-table-lspace: 0pt;
        mso-table-rspace: 0pt;
        background-color: #f6f6f6;
        width: 100%;
      "
      width="100%"
      bgcolor="#f6f6f6"
    >
      <tr>
        <td
          style="font-family: sans-serif; font-size: 14px; vertical-align: top"
          valign="top"
        >
          &nbsp;
        </td>
        <td
          class="container"
          style="
            font-family: sans-serif;
            font-size: 14px;
            vertical-align: top;
            display: block;
            max-width: 580px;
            padding: 10px;
            width: 580px;
            margin: 0 auto;
          "
          width="580"
          valign="top"
        >
          <div
            class="content"
            style="
              box-sizing: border-box;
              display: block;
              margin: 0 auto;
              max-width: 580px;
              padding: 10px;
            "
          >
            <!-- START CENTERED WHITE CONTAINER -->
            <table
              role="presentation"
              class="main"
              style="
                border-collapse: separate;
                mso-table-lspace: 0pt;
                mso-table-rspace: 0pt;
                background: #ffffff;
                border-radius: 7px;
                width: 100%;
                background-image: linear-gradient(
                  200deg,
                  rgb(20, 46, 140),
                  rgb(76, 231, 245)
                );
              "
              width="100%"
            >
              <!-- START MAIN CONTENT AREA -->
              <tr>
                <td
                  class="wrapper"
                  style="
                    font-family: sans-serif;
                    font-size: 14px;
                    vertical-align: top;
                    box-sizing: border-box;
                    padding: 20px;
                  "
                  valign="top"
                >
                  <table
                    role="presentation"
                    border="0"
                    cellpadding="0"
                    cellspacing="0"
                    style="
                      border-collapse: separate;
                      mso-table-lspace: 0pt;
                      mso-table-rspace: 0pt;
                      width: 100%;
                    "
                    width="100%"
                  >
                    <tr>
                      <td
                        style="
                          border: 3px solid white;
                          border-radius: 7px;
                          padding: 10px;
                          font-family: Ubuntu Mono, monospace;
                          font-size: 14px;
                          vertical-align: top;
                        "
                        valign="top"
                      >
                        <p
                          style="
                            font-family: system-ui, -apple-system, Segoe UI,
                              Roboto, Helvetica Neue, Arial, Noto Sans;
                            font-size: 40px;
                            font-weight: 500;
                            margin: 0;
                            margin-bottom: 15px;
                            color: white;
                          "
                        >
                          Registration Successful
                        </p>
                        <p
                          style="
                            font-family: system-ui, -apple-system, Segoe UI,
                              Roboto, Helvetica Neue, Arial, Noto Sans;
                            font-size: 16px;
                            font-weight: normal;
                            margin: 0;
                            margin-bottom: 15px;
                          "
                        >
                          This automated message signifies that registration was
                          successful. <br />
                          You will receive the announcement mail with Tournament
                          details soon!
                        </p>

                        <p
                          style="
                            font-family: system-ui, -apple-system, Segoe UI,
                              Roboto, Helvetica Neue, Arial, Noto Sans;
                            font-size: 15px;
                            font-weight: normal;
                            margin: 0;
                            margin-bottom: 15px;
                            color: black;
                          "
                        >
                          By: <br />Sports Tournament Council
                        </p>
                      </td>
                    </tr>
                  </table>
                </td>
              </tr>

              <!-- END MAIN CONTENT AREA -->
            </table>
            <!-- END CENTERED WHITE CONTAINER -->

            <!-- START FOOTER -->
            <div
              class="footer"
              style="
                clear: both;
                margin-top: 10px;
                color: #3498db;
                text-align: center;
                width: 100%;
              "
            >
              <table
                role="presentation"
                border="0"
                cellpadding="0"
                cellspacing="0"
                style="
                  border-collapse: separate;
                  mso-table-lspace: 0pt;
                  mso-table-rspace: 0pt;
                  width: 100%;
                "
                width="100%"
              >
                <tr>
                  This is an automated message from PyBot. Please do not reply
                  to this email.
                </tr>
              </table>
            </div>
            <!-- END FOOTER -->
          </div>
        </td>
        <td
          style="font-family: sans-serif; font-size: 14px; vertical-align: top"
          valign="top"
        >
          &nbsp;
        </td>
      </tr>
    </table>
  </body>
</html>

    """,
        subtype="html",
    )

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)


def temp_2(rec, subject):

    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = "PyBot(do-not-reply)"
    msg["To"] = str(rec)

    msg.set_content("Do not reply to this email")

    msg.add_alternative(
        """
    <!DOCTYPE html>
<html>
<head>
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
  <title>Automated Reply from PyBot</title>
  <style>
    @media only screen and (max-width: 620px) {
      table.body h1 {
        font-size: 28px !important;
        margin-bottom: 10px !important;
      }

      table.body p,
      table.body ul,
      table.body ol,
      table.body td,
      table.body span,
      table.body a {
        font-size: 16px !important;
      }

      table.body .wrapper,
      table.body .article {
        padding: 10px !important;
      }

      table.body .content {
        padding: 0 !important;
      }

      table.body .container {
        padding: 0 !important;
        width: 100% !important;
      }

      table.body .main {
        border-left-width: 0 !important;
        border-radius: 0 !important;
        border-right-width: 0 !important;
      }

      table.body .btn table {
        width: 100% !important;
      }

      table.body .btn a {
        width: 100% !important;
      }

      table.body .img-responsive {
        height: auto !important;
        max-width: 100% !important;
        width: auto !important;
      }
    }
    @media all {
      .ExternalClass {
        width: 100%;
      }

      .ExternalClass,
      .ExternalClass p,
      .ExternalClass span,
      .ExternalClass font,
      .ExternalClass td,
      .ExternalClass div {
        line-height: 100%;
      }

      .apple-link a {
        color: inherit !important;
        font-family: inherit !important;
        font-size: inherit !important;
        font-weight: inherit !important;
        line-height: inherit !important;
        text-decoration: none !important;
      }

      # MessageViewBody a {
        color: inherit;
        text-decoration: none;
        font-size: inherit;
        font-family: inherit;
        font-weight: inherit;
        line-height: inherit;
      }

      .btn-primary table td:hover {
        background-color: #34495e !important;
      }

      .btn-primary a:hover {
        background-color: #3455db !important;
        border-color: #3455db !important;
      }
      .btnhr a:hover {
        background-color: #14b353 !important;
        border-color: #14b353 !important;
      }
      .btncd a:hover {
        background-color: #4d4d4d !important;
        border-color: #4d4d4d !important;
      }
    }
  </style>
</head>
<body
class=""
style="
background-color: #f6f6f6;
font-family: sans-serif;
-webkit-font-smoothing: antialiased;
font-size: 14px;
line-height: 1.4;
margin: 0;
padding: 0;
-ms-text-size-adjust: 100%;
-webkit-text-size-adjust: 100%;
"
>
<span
class="preheader"
style="
color: transparent;
display: none;
height: 0;
max-height: 0;
max-width: 0;
opacity: 0;
overflow: hidden;
mso-hide: all;
visibility: hidden;
width: 0;
"
>You have deregistered.</span
>
<table
role="presentation"
border="0"
cellpadding="0"
cellspacing="0"
class="body"
style="
border-collapse: separate;
mso-table-lspace: 0pt;
mso-table-rspace: 0pt;
background-color: #f6f6f6;
width: 100%;
"
width="100%"
bgcolor="#f6f6f6"
>
<tr>
  <td
  style="font-family: sans-serif; font-size: 14px; vertical-align: top"
  valign="top"
  >
  &nbsp;
</td>
<td
class="container"
style="
font-family: sans-serif;
font-size: 14px;
vertical-align: top;
display: block;
max-width: 580px;
padding: 10px;
width: 580px;
margin: 0 auto;
"
width="580"
valign="top"
>
<div
class="content"
style="
box-sizing: border-box;
display: block;
margin: 0 auto;
max-width: 580px;
padding: 10px;
"
>
<!-- START CENTERED WHITE CONTAINER -->
<table
role="presentation"
class="main"
style="
border-collapse: separate;
mso-table-lspace: 0pt;
mso-table-rspace: 0pt;
background: #ffffff;
border-radius: 7px;
width: 100%;
background-image: linear-gradient(
  200deg,
  rgb(20, 46, 140),
  rgb(76, 231, 245)
);
"
width="100%"
>
<!-- START MAIN CONTENT AREA -->
<tr>
  <td
  class="wrapper"

  style="
  font-family: sans-serif;
  font-size: 14px;
  vertical-align: top;
  box-sizing: border-box;
  padding: 20px;
  "
  valign="top"
  >
  <table
  role="presentation"
  border="0"
  cellpadding="0"
  cellspacing="0"
  style="
  border-collapse: separate;
  mso-table-lspace: 0pt;
  mso-table-rspace: 0pt;
  width: 100%;
  "
  width="100%"
  >
  <tr>
    <td
    style="
    border: 3px solid white;
    border-radius: 7px;
    padding: 10px;
    font-family: Ubuntu Mono, monospace;
    font-size: 14px;
    vertical-align: top;
    "
    valign="top"
    >
    <p
    style="
    font-family: system-ui, -apple-system, Segoe UI,
    Roboto, Helvetica Neue, Arial, Noto Sans;
    font-size: 40px;
    font-weight: 500;
    margin: 0;
    margin-bottom: 15px;
    color: white;
    "
    >
    You have Deregistered
  </p>
  <p
  style="
  font-family: system-ui, -apple-system, Segoe UI,
  Roboto, Helvetica Neue, Arial, Noto Sans;
  font-size: 16px;
  font-weight: normal;
  margin: 0;
  margin-top: 40px;
  margin-bottom: 15px;
  color: white;
  "
  >

  This automated message signifies that you have deregistered from Sports Tournament.<br>
  You will not receive any follow-up emails related to the Tournament from now.
  <br>
  Wish to register? <a style="color: Blue;text-decoration: none;" href="http://127.0.0.1:5000/">Click here.</a>
</p>

<p
style="
font-family: system-ui, -apple-system, Segoe UI,
Roboto, Helvetica Neue, Arial, Noto Sans;
font-size: 15px;
font-weight: normal;
margin: 0;
margin-top: 40px;
margin-bottom: 15px;
color: black;
"
>
By: <br />Sports Tournament Council
</p>
</td>
</tr>
</table>
</td>
</tr>

<!-- END MAIN CONTENT AREA -->
</table>
<!-- END CENTERED WHITE CONTAINER -->

<!-- START FOOTER -->
<div
class="footer"
style="
clear: both;
margin-top: 10px;
color: #3498db;
text-align: center;
width: 100%;
"
>
<table
role="presentation"
border="0"
cellpadding="0"
cellspacing="0"
style="
border-collapse: separate;
mso-table-lspace: 0pt;
mso-table-rspace: 0pt;
width: 100%;
"
width="100%"
>
<tr>
  This is an automated message from PyBot. Please do not reply
  to this email.
</tr>
</table>
</div>
<!-- END FOOTER -->
</div>
</td>
<td
style="font-family: sans-serif; font-size: 14px; vertical-align: top"
valign="top"
>
&nbsp;
</td>
</tr>
</table>
</body>
</html>
    """, subtype="html",)
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)


def sendmail(rec, subject, template):
    if(template == 1):
        temp_1(rec, subject)
    if(template == 2):
        temp_2(rec, subject)


