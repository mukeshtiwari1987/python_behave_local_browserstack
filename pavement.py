from paver.easy import *
from paver.setuputils import setup
import multiprocessing

setup(
    name = "behave-browserstack",
    version = "0.1.0",
    author = "BrowserStack",
    author_email = "support@browserstack.com",
    description = ("Behave Integration with BrowserStack"),
    license = "MIT",
    keywords = "example selenium browserstack",
    url = "https://github.com/browserstack/lettuce-browserstack",
    packages=['features']
)

def run_behave_test(config, task_id=0):
    sh('CONFIG_FILE=config/%s.json TASK_ID=%s behave' % (config, task_id))

@task
@consume_nargs(1)
def run(args):
    """Run single, local and parallel test using different config."""
    if args[0] in ('local', 'browserstack'):
        run_behave_test(args[0])

@task
def test():
    """Run all tests"""
    sh("paver run local")
    sh("paver run browserstack")