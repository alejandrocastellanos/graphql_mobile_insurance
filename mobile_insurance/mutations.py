import graphene
from typing import Dict, Any


class MobileInsuranceInput(graphene.InputObjectType):
    brand = graphene.String()
    model = graphene.String()
    storage = graphene.String()


class InsuranceMobileMutation(graphene.Mutation):
    ok = graphene.Boolean()
    monthly_insurance_price = graphene.String()
    annual_insurance_price = graphene.String()

    class Arguments:
        mobile_insurance_data = MobileInsuranceInput(required=True)
        email = graphene.String(required=True)
        phone = graphene.String(required=True)

    async def mutate(self, info, mobile_insurance_data: Dict[str, Any], email, phone):

        return InsuranceMobileMutation(ok=True, monthly_insurance_price='', annual_insurance_price='')
