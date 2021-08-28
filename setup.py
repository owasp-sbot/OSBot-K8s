import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    version                       = "0.1.0"               , # change this on every release
    name                          = "osbot_k8s"  ,
    author                        = "Dinis Cruz",
    author_email                  = "dinis.cruz@owasp.org",
    description                   = "OWASP Security Bot - K8s (Kubernetes)",
    long_description              = long_description,
    long_description_content_type = "text/markdown",
    url                           = "https://github.com/owasp-sbot/OSBot-K8s",
    packages                      = setuptools.find_packages(),
    classifiers                   = [ "Programming Language :: Python :: 3"   ,
                                      "License :: OSI Approved :: MIT License",
                                      "Operating System :: OS Independent"   ])
