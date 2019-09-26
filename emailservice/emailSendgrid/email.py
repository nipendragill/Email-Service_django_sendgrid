import os
import sendgrid
from sendgrid.helpers.mail import Mail, Substitution, Attachment, Content, Personalization
from .error import Error
from rest_framework import status


class Email:

    @staticmethod
    def send_email(receivers, subject, content, template_id=None, text_replacements=None,
                   sender_name=None, sender_email=None,
                   attachments=None, cc_list=None, bcc_list=None):
        sendgrid_client = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))
        sender = sendgrid.Email(name=sender_name, email=sender_email)
        mail = Mail(from_email=sender, subject=subject, content=content)

        personalization = Personalization()

        if len(receivers) == 0:
            error = Error({'detail':'Please enter receiver mailId'},
                          status=status.HTTP_400_BAD_REQUEST)
            return error, None
        else:
            for receiver in receivers:
                personalization.add_to(receiver)
        personalization.add_to(receivers[0])

        for cc in cc_list and cc_list is not None:
            personalization.add_cc(cc)

        for bcc in bcc_list and bcc_list is not None:
            personalization.add_bcc(bcc)

        mail.add_personalization(personalization)

        if text_replacements is not None:
            for text_replacement in text_replacements:
                for key, value in text_replacement.items():
                    mail.personalizations[0].add_substitution(Substitution(key, value))
        mail.template_id = template_id

        if attachments is not None:
            for attachment in attachments:
                mail.add_attachment(attachment)

        response = sendgrid_client.client.mail.send.post(request_body=mail.get())
        return {'status': True, 'response': response.body.decode().strip()}