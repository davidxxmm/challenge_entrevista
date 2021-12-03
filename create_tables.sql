CREATE TABLE public.sql_empresas (
	id_empresa int4 NOT NULL,
	nombre_empresa varchar NULL,
	CONSTRAINT sql_empresas_pk PRIMARY KEY (id_empresa)
);

/////// crea tabla de usuarios

CREATE TABLE public.sql_usuarios (
	id_usuario int4 NOT NULL,
	id_empresa int4 NOT NULL,
	nombre varchar NULL,
	CONSTRAINT sql_usuarios_pk PRIMARY KEY (id_usuario, id_empresa)
);


-- public.sql_usuarios foreign keys

ALTER TABLE public.sql_usuarios ADD CONSTRAINT sql_usuarios_fk FOREIGN KEY (id_empresa) REFERENCES public.sql_empresas(id_empresa); 
          
        
///// crear tabla de movimientos

CREATE TABLE public.sql_movimientos (
	id_movimiento serial4 NOT NULL,
	id_usuario int4 NULL,
	cantidad_ha int4 NULL,
	creacion2 timestamp NULL,
	CONSTRAINT sql_movimientos_pk PRIMARY KEY (id_movimiento)
);
