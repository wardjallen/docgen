import logging
import distutils
from random import choices


from webexteamssdk.models.cards import Colors, TextBlock, FontWeight, FontSize, Column, AdaptiveCard, ColumnSet, \
    Text, Image, HorizontalAlignment, Toggle, Choices
from webexteamssdk.models.cards.actions import Submit

from webex_bot.formatting import quote_info, html_link
from webex_bot.models.command import Command
from webex_bot.models.response import response_from_adaptive_card, Response
from generate import generate_doc
log = logging.getLogger(__name__)

sow_template = "./templates/RFP Technical Responses.docx"

class SOW(Command):
    def __init__(self):
        super().__init__(
            command_keyword="sow",
            help_message="Generate SOW Technical Docs!",
            chained_commands=[SowCallback()])
        

    def execute(self, message, attachment_actions, activity):

        text1 = TextBlock("Generate SOW Tech Docs", weight=FontWeight.BOLDER, size=FontSize.MEDIUM, horizontalAlignment="Center")
        customer = Text(id="customer", placeholder="Customer Name")
        ucm = Toggle(title="UCM", id="ucm")
        cuc = Toggle(title="Unity Connection", id="cuc")
        imp = Toggle(title="Presence Server", id="imp")
        cer = Toggle(title="Emergency Responder", id="cer")
        exp = Toggle(title="Expressways", id="expressways")
        endpoints = Toggle(title="Endpoints", id="endpoints")
        ucm_cloud = Toggle(title="UCM-Cloud", id="ucm_cloud")
        ucm_cloud_g = Toggle(title="UCM-Cloud-G", id="ucm_cloud_g")
        on_premise = Toggle(title="On Premise", id="on_premise")
        webex_meetings = Toggle(title="Webex Meetings", id="webex_meetings")
        efax = Toggle(title="EFax", id="efax")
        cisco_8851 = Toggle(title="Cisco 8851", id="cisco_8851")
        cisco_7841 = Toggle(title="Cisco 7841", id="cisco_7841")
        cisco_7832 = Toggle(title="Cisco 7832", id="cisco_7832")
        call_recording = Toggle(title="Call Recording", id="call_recording")
        fax_text = TextBlock("If Fax enter either Imagicle or StoneFax", horizontalAlignment="Center")
        efax_partner = Text(id="efax_partner", placeholder="Imagicle or StoneFax")
        efax_endpoints = Text(id="fax_endpoints", placeholder="Enter the Number or Fax Endpoints to configure")
        efax_email_integrations = Text(id="fax_email_integrations", placeholder="Enter the Number or Fax Email Integrations to configure")
        num_aa_text = TextBlock("If Unity Connection", horizontalAlignment="Center")
        num_aa = Text(id="num_aa", placeholder="Enter the Number of Auto attendants")
        num_ch = Text(id="num_ch", placeholder="Enter the Number of Call Handlers")
        call_recording_text = TextBlock("If Call Recording", horizontalAlignment="Center")
        recording_channels = Text(id="recording_channels", placeholder="Enter the Number of Recording Channels")
        customer_name_column = Column(items=[customer], width=2)
        ucm_column = Column(items=[ucm], width=2)
        cuc_column = Column(items=[cuc], width=2)
        imp_column = Column(items=[imp], width=2)
        cer_column = Column(items=[cer], width=2)
        exp_column = Column(items=[exp], width=2)
        endpoints_column = Column(items=[endpoints], width=2)
        ucm_cloud_column = Column(items=[ucm_cloud], width=2)
        ucm_cloud_g_column = Column(items=[ucm_cloud_g], width=2)
        on_premise_column = Column(items=[on_premise], width=2)
        webex_meetings_column = Column(items=[webex_meetings], width=2)
        cisco_8851_column = Column(items=[cisco_8851], width=2)
        cisco_7841_column = Column(items=[cisco_7841], width=2)
        cisco_7832_column = Column(items=[cisco_7832], width=2)
        efax_column = Column(items=[efax], width=2)
        efax_endpoints_column = Column(items=[efax_endpoints], width=2)
        efax_email_integrations_column = Column(items=[efax_email_integrations], width=2)
        call_recording_column = Column(items=[call_recording], width=2)
        efax_partner_column = Column(items=[efax_partner], width=2)
        num_aa_column = Column(items=[num_aa], width=2)
        num_ch_column = Column(items=[num_ch], width=2)
        recording_channels_column = Column(items=[recording_channels], width=2)


        

        submit = Submit(title="Submit",
                        data={
                            "callback_keyword": "sow_callback"})

        card = AdaptiveCard(
            body=[ColumnSet(columns=[Column(items=[text1], width=2)]),
                  ColumnSet(columns=[customer_name_column]),
                  ColumnSet(columns=[ucm_cloud_column, ucm_cloud_g_column]),
                  ColumnSet(columns=[ucm_column, cuc_column, imp_column]),
                  ColumnSet(columns=[cer_column, exp_column, endpoints_column]),
                  ColumnSet(columns=[on_premise_column, efax_column, call_recording_column]),
                  ColumnSet(columns=[webex_meetings_column]),
                  ColumnSet(columns=[cisco_8851_column, cisco_7841_column, cisco_7832_column]),
                  ColumnSet(columns=[Column(items=[fax_text], width=2)]),
                  ColumnSet(columns=[efax_partner_column]),
                  ColumnSet(columns=[efax_endpoints_column]),
                  ColumnSet(columns=[efax_email_integrations_column]),
                  ColumnSet(columns=[Column(items=[num_aa_text], width=2)]),
                  ColumnSet(columns=[num_aa_column]),
                  ColumnSet(columns=[num_ch_column]),
                  ColumnSet(columns=[Column(items=[call_recording_text], width=2)]),
                  ColumnSet(columns=[recording_channels_column]),
                  ], actions=[submit])

        return response_from_adaptive_card(card)

class SowCallback(Command):

    def __init__(self):
        super().__init__(
            card_callback_keyword="sow_callback",
            delete_previous_message=True)

    def pre_execute(self, message, attachment_actions, activity):
  
        text1 = TextBlock("Working on it....", weight=FontWeight.BOLDER, wrap=True, size=FontSize.DEFAULT,
                          horizontalAlignment=HorizontalAlignment.CENTER, color=Colors.DARK)
        text2 = TextBlock("I am busy working on your request. Please continue to look busy while I do your work.",
                          wrap=True, color=Colors.DARK)
        card = AdaptiveCard(
            body=[ColumnSet(columns=[Column(items=[text1, text2])]),
                  ])

        return response_from_adaptive_card(card)

    def execute(self, message, attachment_actions, activity):
        data = dict(attachment_actions.inputs.items())
        data.pop('callback_keyword')
        for k, v in data.items():
            print(k, v)
            try:
                data[k] = bool(distutils.util.strtobool(v))
            except:
                pass
        generate_doc(sow_template,"sow", data)
        res = Response()
        customer = attachment_actions.inputs.get("customer")
        res.text = f"Here is the Generated Doc for {customer}. Please go over and double check."
        res.files = "sow.docx"
        return res
