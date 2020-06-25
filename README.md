# eventbridge-integration-solution-zendesk-ticket-translations
## Amazon EventBridge Integration Solution: Translating Zendesk Tickets

This Quick Start deploys an integration with AWS Step Functions, AWS Lambda, and Amazon Translate for Amazon EventBridge SaaS Partner Integrations with Zendesk. This solution leverages Zendesk events, sending them to an Amazon EventBridge event bus that uses a rule to evaluate "Comment Created" events and targets a Step Functions execution when events are match. Once sent to Step Functions, Lambdas are invoked that:

1) get the ticket information, including the comment

2) determine the source language and translate the ticket using Amazon Translate to a language you prefer

3) update the ticket with an 'internal' comment

![Quick Start architecture for EventBridge Integration Solution: Zendesk Translate](https://github.com/aws-quickstart/eventbridge-integration-solution-zendesk-ticket-translations/raw/master/images/eventbridge-zendesk-translate.png)


To post feedback, submit feature ideas, or report bugs, use the **Issues** section of [this GitHub repo](https://github.com/aws-quickstart/eventbridge-integration-solution-zendesk-ticket-translations).