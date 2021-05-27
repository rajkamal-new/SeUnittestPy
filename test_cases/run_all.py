import os
import unittest
import HtmlTestRunner

def run_all_tests():

    suite = unittest.TestSuite()

    all_test_cases = unittest.defaultTestLoader.discover("test_cases",'test*.py')


    for test_case in all_test_cases:
        suite.addTests(test_case)

    with open(os.path.abspath(os.getcwd() + "/../target/Reports/HTML_Test_Runner_ReportTest.html"), "w") as output_file:
        html_runner = HtmlTestRunner.HTMLTestRunner(
            output="../target/Reports/",
            stream=output_file,
            report_title='Basic Functional Tests'
        )

        html_runner.run(suite)

if __name__ == '__main__':
    run_all_tests()