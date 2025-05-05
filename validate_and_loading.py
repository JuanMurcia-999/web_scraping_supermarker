import pandas as pd
from config import engine

final_df=pd.DataFrame()

fail_prodct=[]


def create_dataset(products,hierarchy):
    print('🔼 cargando datos')
    data=[] 
    try:
        for product in products:
            try:
                data.append(extract_info(product,hierarchy))
            except Exception as e:
                fail_prodct.append(product)
        temp_df=pd.DataFrame(data)
        temp_df.to_sql("products", engine, if_exists='append', index=False)
        engine.dispose()
    except Exception as e:
        print('🔴  falla en la base de datos')



def extract_info(product,hierarchy):
    return {
        'score': product.get('aggregateRating',{}).get('ratingValue',0),
        'brand': product.get('brand', {}).get('name', 'N/D'),
        'sku': product.get('sku', 'N/D'),
        'price': product.get('offers', {}).get('price', 0),
        'availability': product.get('offers', {}).get('availability', 'N/D'),
        'url': 'https://www.homecenter.com.co/'+product.get('offers', {}).get('url', 'N/D'),
        'image': product.get('image', 'N/D'),
        'name': product.get('name', 'N/D'),
        'section':hierarchy.get('section_name','N/D') ,
        'family':hierarchy.get('family_name','N/D'),
        'category':hierarchy.get('category','N/D'),
        'sub_category':hierarchy.get('sub_category','N/A')
    }



