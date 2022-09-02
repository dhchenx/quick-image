from quick_pypi.deploy import *

auto_deploy(
    cwd=os.path.dirname(os.path.realpath(__file__)),
    name="quick-image",
    long_name="Quick Image",
    description="A simple and rapid image processing toolkit",
    long_description="A simple and rapid image processing toolkit",
    src_root="src",
    dists_root=f"dists",
    pypi_token='D:/GitHub/pypi_upload_token.txt',
    test=False,
    version="0.0.1a0",
    project_url="http://github.com/dhchenx/quick-image",
    author_name="Donghua Chen",
    author_email="douglaschan@126.com",
    requires="", # use ; for multiple requires
    license='MIT',
    license_filename='LICENSE',
    keywords="image processing",
    github_username="dhchenx",
    readme_path="README.md",
   # only_build=True
   # console_scripts=""
)

