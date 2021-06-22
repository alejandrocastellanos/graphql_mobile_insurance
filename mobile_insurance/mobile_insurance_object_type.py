import graphene


class MobileInsuranceObjectType(graphene.ObjectType):
    brand = graphene.String()
    model = graphene.String()
    storage = graphene.String()
