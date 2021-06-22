import graphene

from mobile_insurance.mobile_insurance_object_type import MobileInsuranceObjectType
from mobile_insurance.mutations import InsuranceMobileMutation


class Query(graphene.ObjectType):

    insurance_mobile = graphene.List(MobileInsuranceObjectType, brand=graphene.String(required=False),
                                     model=graphene.String(required=False), storage=graphene.String(required=False))

    @staticmethod
    async def resolve_insurance_mobile(self, info, brand=None, model=None, storage=None):
        status_list = [
            {'brand': 'Apple'}
        ]
        return status_list


class Mutation(graphene.ObjectType):
    mobile_insurance = InsuranceMobileMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
