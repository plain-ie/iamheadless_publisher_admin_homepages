# iamheadless_publisher_admin_homepages

App to render homepage item type in `iamheadless_publisher_admin` frontend.

## Installation

Requires `iamheadless_publisher_admin`

1. install package
2. add `iamheadless_publisher_admin_homepages` to `INSTALLED_APPS` in `settings.py`
3. add viewsets to `IAMHEADLESS_PUBLISHER_ADMIN_VIEWSET_LIST` in `settings.py`
```
[
    'iamheadless_publisher_admin_homepages.viewsets.HomepageCreateViewSet',
    'iamheadless_publisher_admin_homepages.viewsets.HomepageDeleteViewSet',
    'iamheadless_publisher_admin_homepages.viewsets.HomepageRetrieveUpdateViewSet',
]
```
