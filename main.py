from fastapi import FastAPI
from app.core.settings import settings
from app.router.trains import trains_router
from app.router.passengers import passenger_router
from scalar_fastapi import get_scalar_api_reference

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION
)

app.include_router(trains_router, prefix="/api")
app.include_router(passenger_router, prefix="/api")

@app.get("/scalar")
def scalar_api_reference():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title=app.title
    )
 