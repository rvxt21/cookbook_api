import typing

if typing.TYPE_CHECKING:
    from users.models import User


def create_user(
    email: str,
    password: str = "",
    first_name: str = "",
    surname: str = "",
    is_staff: bool = False,
    is_superuser: bool = False,
    is_active: bool = True,
    **extra_fields,
) -> "User":
    from users.models import User

    user = User(
        email=email,
        first_name=first_name,
        surname=surname,
        is_superuser=is_superuser,
        is_staff=is_staff,
        is_active=is_active,
        **extra_fields,
    )

    if password:
        user.set_password(password)
    else:
        user.set_unusable_password()

    user.full_clean()
    user.save()
    return user
