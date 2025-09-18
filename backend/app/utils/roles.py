from fastapi import Depends, HTTPException, status
from app.utils.security import get_current_user
from app.models.user import User

def require_role(allowed_roles: list[User]):
    def role_checker(user: User = Depends(get_current_user)):
        print("\n\n\n-------------------------------\n")
        print("allowed_roles: ")
        print(allowed_roles)
        print("\n")
        print("type(user): ")
        print(type(user))
        print("\n")
        print("\n\n\n-------------------------------\n")
        if not any(isinstance(user, role) for role in allowed_roles): 
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You do not have access to this resource",
            )
        return user
    return role_checker