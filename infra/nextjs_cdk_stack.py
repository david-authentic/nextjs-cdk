from aws_cdk import (
    Stack,
    SecretValue,
    aws_amplify_alpha as amplify
)
from constructs import Construct

class NextjsStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        amplify_app = amplify.App(self, "Nextjs",
                                  source_code_provider=amplify.GitHubSourceCodeProvider(
                                      owner="david-authentic",
                                      repository="nextjs-cdk",
                                      oauth_token=SecretValue.secrets_manager(
                                          secret_id="arn:aws:secretsmanager:us-east-1:875073938755:secret:github-token-4059es"
                                      ),
                                  ),
                                  auto_branch_deletion=True,
                                  )

        main = amplify_app.add_branch("main")
        main.add_environment("BUILD_ENV", "production")

        dev = amplify_app.add_branch("staging")
        dev.add_environment("BUILD_ENV", "staging")
