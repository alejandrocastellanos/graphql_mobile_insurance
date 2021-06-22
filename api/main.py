from graphql.execution.executors.asyncio import AsyncioExecutor
from starlette.applications import Starlette
from starlette.graphql import GraphQLApp
from graphql.execution import ExecutionResult
from starlette.middleware.cors import CORSMiddleware
from uvicorn.middleware.proxy_headers import ProxyHeadersMiddleware

import settings
from api.schema import schema


class PakkunGraphQLAPP(GraphQLApp):

    async def execute(self, query, variables=None, context=None, operation_name=None):
        if settings.DEBUG is False and '__schema' in query:
            return ExecutionResult(data=None, errors=[ValueError('schema is not available')])
        return await super().execute(query, variables, context, operation_name)


app = Starlette()
app.add_middleware(CORSMiddleware, allow_origins=['*'], allow_methods=['GET', 'POST'], allow_headers=['*'])
app.add_middleware(ProxyHeadersMiddleware)
app.add_route(
    path='/mobile_insurance/graphql',
    route=PakkunGraphQLAPP(schema=schema, executor_class=AsyncioExecutor, graphiql=settings.DEBUG)
)
