from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Driver, TaxiCompany

@api_view(['POST'])
def update_driver_availability(request):
    driver_id = request.data.get('driver_id')
    company_id = request.data.get('company_id')
    driver = Driver.objects.get(id=driver_id)
    company = TaxiCompany.objects.get(id=company_id)
    
    driver.set_availability(company=company)
    return Response({"status": "success", "message": "Availability updated"})
